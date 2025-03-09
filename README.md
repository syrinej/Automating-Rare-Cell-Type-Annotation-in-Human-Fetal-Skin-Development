# Automating Rare Cell Type Annotation in Human Fetal Skin Development

This project provides an automated solution via a web-based interface for annotating rare cell types from single-cell RNA sequencing (scRNA-seq) data, specifically targeting human fetal skin development.

---

##  Project Objectives

- **Complete Automation:** Streamline data preprocessing, automate prediction of rare cell types using a pre-trained Machine Learning model, and generate interactive visualizations.
- **Accessibility:** User-friendly web interface for researchers without extensive bioinformatics expertise.
- **Applicability:** Precise annotation of rare cells in human fetal skin to support developmental biology research.

---

##  Data Source

- **Repository:** [Gene Expression Omnibus (GEO)](https://www.ncbi.nlm.nih.gov/geo/)
- **GEO Accession Number:** `GSE179565`
- **Data Type:** Human fetal skin scRNA-seq dataset.

---

## ⚙️ Methodology and Key Steps

### 1️- Automated Data Preprocessing

- **Filtering:** Remove low-quality cells and rarely expressed genes (`Scanpy`).
- **Normalization and Scaling:** Normalize gene expression values for comparability (`Scanpy`).
- **Dimensionality Reduction:** PCA to reduce complexity (`Scanpy`).
- **Clustering:** Leiden algorithm to identify cell clusters (`Scanpy`).

### 2️- Machine Learning-Based Automated Annotation

- **Model Training:** Random Forest classifier trained on manually annotated data (`scikit-learn`).
- **Model Serialization:** Saved model for future use (`joblib`).
- **Performance Evaluation:** Accuracy evaluation using confusion matrix and metrics.

### 3️- User-Friendly Web Interface Development

- **Frontend Development:** Built with Flask, Bootstrap, and HTML/CSS.
- **Interactive Visualizations:** UMAP plots for intuitive exploration (`Plotly`).
- **Data Accessibility:** Easy data upload and download functionality for annotated results.

---

##  How to Use the Tool

### Prerequisites
- Python ≥ 3.8
- Recommended: virtual environment (`conda` or `venv`)

### Quick Installation
```bash
git clone <repository-url>
cd <repository-name>
pip install -r requirements.txt
python app.py


