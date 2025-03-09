Automating Rare Cell Type Annotation in Human Fetal Skin Development

Project Overview
This project automates the annotation of rare cell types from single-cell RNA sequencing (scRNA-seq) data, specifically in the context of human fetal skin development. It integrates machine learning techniques, advanced bioinformatics processing, and an interactive web interface to streamline annotation workflows.

Objectives
- Machine Learning Model: Developed a Random Forest classifier to accurately predict cell types based on gene expression profiles.
- Automated Data Processing: Implemented comprehensive preprocessing steps including filtering, normalization, scaling, dimensionality reduction (PCA), and clustering (Leiden algorithm).
- User-Friendly Interface: Built a responsive web-based tool enabling researchers to upload datasets, automatically perform annotation, and visualize results interactively.

Data Source
- Dataset: Single-cell RNA-seq data from human fetal skin (GEO accession: GSE179565).
- Tools Used for Data Retrieval: GEOquery (R), requests, pandas.

 Methodology
 Data Preprocessing
- Inspection & Filtering: Used scanpy and pandas to manage datasets, remove low-quality cells, and reduce data noise.
- Normalization & Scaling: Applied methods such as normalize_total, log1p, and data scaling using Scanpy.
- Dimensionality Reduction: Performed PCA for feature extraction.

 Annotation & Model Training
- Clustering: Identified cell clusters using the Leiden algorithm.
- Marker Genes: Used Scanpy's rank_genes_groups and the CellMarker database for manual cell type annotation.
- Model Development: Trained a Random Forest classifier (using scikit-learn) on manually annotated data, achieving automated and reproducible cell type predictions.

Web Interface
- Framework: Developed using Flask.
- Visualization: Generated interactive UMAP plots with Plotly for intuitive visualization of annotated cells.
- Accessibility: Easy-to-use file upload/download features supported by HTML/CSS and Bootstrap for responsive design.

 Tools & Technologies
- Data Processing: Scanpy, pandas, CellMarker
- Machine Learning: scikit-learn, joblib
- Web Development: Flask, Plotly, Bootstrap, HTML/CSS

Results
- Developed a robust pipeline to automate and simplify rare cell type annotation.
- Enabled interactive exploration and visualization of single-cell datasets.

