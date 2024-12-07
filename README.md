# Dimensionality Reduction for Filtration Attacks

This repository contains the source code and scripts associated with the paper *Exploring the Effect of Dimensionality Reduction Techniques on Filtration Attacks*. The study focuses on assessing the performance of feature-reduced datasets against original features on various filtration attack scenarios.

The datasets used in this repository were preprocessed and adapted for the study. The original versions can be accessed at the following links: [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html), [CSE-CIC-IDS2018](https://www.unb.ca/cic/datasets/ids-2018.html), and [CERT r4.2](https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247).



Please note that the calculations were conducted in a private cloud environment containing session and credential details in the file paths. To ensure privacy and security, all file paths in the scripts have been anonymized.


## Directory Structure

- **/data_preprocessing/**: Preprocessing script for the UNB CIC-IDS2017 and UNB CSE-CIC-IDS2018 datasets. For CERT r4.2 preprocessing, an open-source granularity extractor algorithm is used. For more details, refer to [this repository](https://github.com/lcd-dal/feature-extraction-for-CERT-insider-threat-test-datasets).


- **/dimensionality_reduction/**: Includes canonical dimensionality reduction scripts for algorithms such as PCA, ICA, and Autoencoders using the scikit-learn library, as well as a custom-implemented Genetic Programming algorithm.

- **/feature_extraction/**: Feature extraction script for the UNB CIC-IDS2017 and UNB CSE-CIC-IDS2018 datasets, extracting specific features based on attack timestamps provided in the dataset documentation. For CERT r4.2, the previously mentioned open-source granularity extractor algorithm is used.


- **/model_training/**: Contains a Random Forest implementation using the scikit-learn library to train and evaluate the performance of datasets with dimensionality-reduced features compared to those with the original features.

- **/processed_data/**: Contains the testing partition of cleaned and preprocessed datasets, including UNB CIC-IDS2017, UNB CSE-CIC-IDS2018, and CERT r4.2 with daily, weekly, and session-based granularity. Due to size constraints, training partitions are not included but can be provided upon request. For access, please email keremalp.durdabak@gmail.com.



## Citation

Please cite the following thesis if you use this repository or reference the concepts herein:

**Keremalp Durdabak, Nur Zincir-Heywood, Malcolm Heywood, et al.**  
"Exploring the Effect of Dimensionality Reduction Techniques on Filtration Attacks."  
Master's Thesis, Dalhousie University, Halifax, Canada, 2023.  
[DOI: http://hdl.handle.net/10222/84358](http://hdl.handle.net/10222/84358)
