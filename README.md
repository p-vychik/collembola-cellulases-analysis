# Phylogeny Project – AK Ebersberger

This repository contains scripts and workflows used for phylogenetic analyses performed in the **Ebersberger Lab**. 
It includes Jupyter notebooks for species tree preparation and tree visualization, as well as a Nextflow pipeline for constructing maximum likelihood gene trees from orthologous sequence datasets.

---

### `species_tree.ipynb`
Jupyter notebook used to:

- Generate a pruned MetaInvert species tree
- Create a sorted species tree for improved visualization of phylogenetic profiles
- Prepare sorting newick trees used for PhyloProfile matrix visualization

---

### `trees_visualizations.ipynb`
Jupyter notebook used for:

- Rendering gene trees inferred with **IQ-TREE2**
- Producing high-resolution SVG visualizations of phylogenetic trees
- Preparing trees for figures and publication-quality graphics

---

### `degaper.py`
Python script used in Nextflow pipeline for filtering MSA columns

---

### `nextflow_workflow/`
A **Nextflow pipeline** for automated phylogenetic tree reconstruction.

The pipeline:

1. Processes two FASTA files containing sequences obtained from separate fDOG ortholog search runs
2. Applies filtering steps to remove problematic sequences and reduce the final ML-tree size while preserving phylogenetic diversity of the species
3. Constructs a multiple sequence alignment
4. Infers maximum likelihood gene trees using **IQ-TREE2**

This workflow enables reproducible large-scale gene tree reconstruction.

---

### `trees/`
Contains **ML gene trees** produced by the `nextflow_workflow` pipeline.

Trees are stored in **NEWICK format** and represent the primary phylogenetic inference results.

---

### `output/`
Contains:

- Final ML gene trees
- Supplementary files generated during tree inference
- Intermediate and processed files used for producing final figures and tree visualizations

---


## Purpose

This repository supports phylogenetic analyses performed as part of a project in **AK Ebersberger**, focusing on gene tree reconstruction and comparative phylogenetic analysis across species.

---

## Notes

The repository mainly contains **analysis scripts and workflows**, fasta with input sequences are not be included.
