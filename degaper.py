#!/usr/bin/env python

import sys

seq = []
dash_columns = {}
out_entries = []
entries_total_number = 0


def find_dash_indices(seq_list):
    i = 0
    indices = []
    while True:
        try:
            index = seq_list.index("-", i)
            indices.append(index)
            i = index + 1
        except ValueError:
            return indices


def update_dash_columns(indices):
    global dash_columns
    if not indices:
        return
    for index in indices:
        if index in dash_columns:
            dash_columns[index] += 1
        else:
            dash_columns[index] = 1


def count_dashes_in_msa_columns(path):
    global seq
    global entries_total_number
    with open(path, 'r') as fin:
        for line in fin:
            if line.startswith(">") and len(seq):
                indices = find_dash_indices(seq)
                update_dash_columns(indices)
                seq = []
                entries_total_number += 1
            elif not line.startswith(">"):
                line = line.strip("\n")
                seq.extend(list(line))
        else:
            indices = find_dash_indices(seq)
            update_dash_columns(indices)
            entries_total_number += 1


def save_cleaned_msa(path, alignment_out_path, columns_to_discard):
    global seq
    global out_entries
    seq = []
    
    with open(alignment_out_path, 'w') as fout:
        with open(path, 'r') as fin:
            for line in fin:
                line = line.strip("\n")
                if line.startswith(">") and len(seq):
                    seq_line = "".join([elem for index, elem in enumerate(seq) if index not in columns_to_discard])
                    if seq_line.count("-") / len(seq_line) > 0.75:
                        out_entries.pop()
                        out_entries.append(line)
                        seq = []
                        continue
                    out_entries.append("".join(seq_line))
                    out_entries.append(line)
                    seq = []
                elif line.startswith(">"):
                    out_entries.append(line)
                else:
                    seq.extend(list(line))
            else:
                seq_line = "".join([elem for index, elem in enumerate(seq) if index not in columns_to_discard])
                if seq_line.count("-") / len(seq_line) < 0.75:
                    out_entries.append(seq_line)
                else:
                    out_entries.pop()
        fout.write("\n".join(out_entries))


def main():
    if len(sys.argv) > 1:
        count_dashes_in_msa_columns(sys.argv[1])
        columns_to_discard = set([column_index for column_index, dash_count in dash_columns.items() if dash_count/entries_total_number > 0.5])
        save_cleaned_msa(sys.argv[1], sys.argv[2], columns_to_discard)
    else:
        print("Wrong number of arguments")


if __name__ == "__main__":
    main()
