"""
Normalize gene expression values and handle missing data.
"""

import pandas as pd
import numpy as np
import os

# Load raw expression data
geo_id = "GSE70970"
expr_df = pd.read_csv(f"../data/{geo_id}_raw_expression.csv", index_col=0)

print("Normalizing expression values with log2 transform...")
expr_df = np.log2(expr_df + 1)  # simple log transform to stabilize variance

# Optional: z-score normalization across samples
expr_df = (expr_df - expr_df.mean(axis=0)) / expr_df.std(axis=0)

# Check for missing values
missing_count = expr_df.isna().sum().sum()
print(f"Missing values in dataset: {missing_count}")
expr_df.fillna(expr_df.mean(), inplace=True)

# Save preprocessed data
os.makedirs("../data", exist_ok=True)
expr_df.to_csv(f"../data/{geo_id}_normalized_expression.csv")
print(f"Preprocessed data saved to data/{geo_id}_normalized_expression.csv")
