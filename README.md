# Dimensionality Reduction for Filtration Attacks

This repository contains the code and scripts for the study *Exploring the Effect of Dimensionality Reduction Techniques on Filtration Attacks*, which assesses feature-reduced datasets against original features in filtration attack scenarios.

The datasets used are [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html), [CSE-CIC-IDS2018](https://www.unb.ca/cic/datasets/ids-2018.html), and [CERT r4.2](https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247), cleaned and adapted for analysis. Calculations were performed on a private cloud environment with session and credential details in the file paths; these have been anonymized for security.

## Directory Structure

- **/scripts/**: Contains the necessary scripts for preprocessing, dimensionality reduction, feature extraction, and model training.
- **/datasets/**: Testing partitions of cleaned datasets (UNB CIC-IDS2017, UNB CSE-CIC-IDS2018, CERT r4.2 with daily, weekly, and session granularity). Training partitions are available upon request: keremalp.durdabak@gmail.com.

## Citation

Please cite the following paper if you use this repository or reference the methodologies applied:

**Keremalp Durdabak, Nur Zincir-Heywood, Malcolm Heywood, et al.**  
"Exploring the Effect of Dimensionality Reduction Techniques on Filtration Attacks"  
IEEE Symposium Series on Computational Intelligence (SSCI 2025), Trondheim, Norway, 2025.