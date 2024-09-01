import os
from flask import Flask, request, render_template, redirect, url_for
import scanpy as sc
import joblib
import plotly.express as px

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = './uploads'
app.config['OUTPUT_FOLDER'] = './outputs'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Load the model
model = joblib.load('model.pkl')

def preprocess_data(file_path):
    # Load the data into an AnnData object
    adata = sc.read(file_path)
    
    # Step 1: Filter out low-quality cells and genes
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    
    # Step 2: Normalize the data
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    
    # Step 3: Scale the data to unit variance and mean zero
    sc.pp.scale(adata, max_value=10)
    
    # Step 4: Perform PCA for dimensionality reduction
    sc.tl.pca(adata, svd_solver='arpack')
    
    return adata

def predict_cell_types(adata):
    predictions = model.predict(adata.X)
    adata.obs['predicted_cell_type'] = predictions
    return adata

def generate_umap(adata):
    sc.tl.umap(adata)
    fig = px.scatter(x=adata.obsm['X_umap'][:, 0], y=adata.obsm['X_umap'][:, 1], color=adata.obs['predicted_cell_type'])
    fig_path = './static/umap_plot.html'
    fig.write_html(fig_path)
    return fig_path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Preprocess the data
        adata = preprocess_data(file_path)
        
        # Predict cell types
        adata = predict_cell_types(adata)
        
        # Generate and save UMAP visualization
        umap_plot_url = generate_umap(adata)
        
        # Save the annotated data
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], f'annotated_{file.filename}')
        adata.write(output_path)
        
        return render_template('results.html', umap_plot_url=umap_plot_url, download_link=output_path)

if __name__ == '__main__':
    app.run(debug=True)
