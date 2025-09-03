import GEOparse
import pandas as pd
import os

# Choose a GEO dataset
geo_id = "GSE70970" 

print(f"Fetching dataset {geo_id} from NCBI GEO...")
gse = GEOparse.get_GEO(geo=geo_id, destdir="../data", silent=False)

# Extract expression matrix
expr_df = gse.pivot_samples('VALUE')
print("\nExpression matrix shape (genes x samples):", expr_df.shape)

print("\nFirst 5 genes:")
print(expr_df.head())

# Basic stats
print("\nBasic stats for gene expression values:")
print(expr_df.describe())

# Save raw expression data for later steps
os.makedirs("../data", exist_ok=True)
expr_df.to_csv(f"../data/{geo_id}_raw_expression.csv")
print(f"\nRaw expression data saved to data/{geo_id}_raw_expression.csv")
