# Persistent Organic Pollutants in Freshwater: Spatial Distribution and Risk Analysis

## Overview
This repository contains all the data processing and analysis conducted for my thesis on the spatial distribution and risk analysis of persistent organic pollutants (POPs) in freshwater ecosystems.

H1: We observe regional differences in ecotoxic risk.
H2: xx compounds are more dangerous than xx compounds.
H3: Compounds demonstrate high persistence according to models.

## Repository Structure
- `data/`: Raw and processed data files used in the analysis.
- `kod/`: Code scripts for data processing and analysis.
- `src/`: Python automation scripts and functions.
- `requirements.txt`: Library list for setting up a virtual environment.

## Installation of Environment
To install an environment using a requirements.txt file, follow these steps:

Ensure you have Python and pip installed on your system.
Navigate to the directory containing your requirements.txt file in the command line.
Run the command 

pip install -r requirements.txt. 


## How to Use
- Data details are in the `data/` folder.
- Run scripts in `kod/` to replicate the analysis.


Here's a brief description of each Jupyter notebook in repository:

**corr_matrix.ipynb**: Contains code for generating a correlation matrix of the PCB, OCP, and PAH dataset.

**data_load.ipynb**: This notebook includes scripts for loading and initially preprocessing the data.

**dendrogram.ipynb**: Contains code for creating dendrogram visualizations, useful in hierarchical clustering analysis.

**distribucije.ipynb**: Focuses on analyzing and visualizing the distributions of concentrations and toxicity.

**logP_median.ipynb**: Deals with calculating and analyzing the median logP values (a measure of lipophilicity) of compounds.

**mapa_karta.ipynb**: Involves mapping or spatial visualization of the data.

**PBT_score.ipynb**: Calculates and analyzes PBT (Persistence, Bioaccumulation, Toxicity) scores for compounds.

**pca_analiza.ipynb**: Contains Principal Component Analysis (PCA) for data dimensionality reduction or exploratory analysis.

**PCA_lokacije_proba.ipynb**: Similar to the above, but focused on PCA for specific locations.

**računanje_TU.ipynb**: Involves calculating Toxic Units (TU) for samples.

**slike_molekula.ipynb**: Generates molecular structures of compounds.

**TU_sed.ipynb**: Focuses on analyzing or calculating Toxic Units for sediment samples.

**TU_site LC50 modeli.ipynb**: Relates to calculating site-specific Toxic Units using LC50 (Lethal Concentration) models.

**VEGA_QSAR_odabir_modela.ipynb**: Selects models from VEGA-QSAR, software for Quantitative Structure-Activity Relationship modeling.

 
## Dependencies
- Python 3.10

## Contact
For any queries related to this research, please contact me at ivananad2@gmail.com.

## Acknowledgments
I would like to thank doc. dr. sc. Mario Lovrić, dr. sc. Snježana Herceg Romanić and prof. dr. sc. Šime Ukić for their guidance and support throughout this research.

