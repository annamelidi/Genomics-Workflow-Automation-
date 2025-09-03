"""
Basic plots of top expressed genes and gene expression distributions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load normalized data
geo_id = "GSE70970"
expr_df = pd.read_csv(f"../data/{geo_id}_normalized_expression.csv", index_col=0)

os.makedirs("../figures", exist_ok=True)

# Top 20 expressed genes (mean across samples)
top_genes = expr_df.mean(axis=1).sort_values(ascending=False).head(20)
plt.figure(figsize=(10,6))
top_genes.plot(kind='bar', color='skyblue')
plt.title("Top 20 expressed genes")
plt.ylabel("Normalized expression")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../figures/top_genes.png")
plt.close()
print("Saved figure: figures/top_genes.png")

# Heatmap of top genes across samples
import seaborn as sns
plt.figure(figsize=(12,8))
sns.heatmap(expr_df.loc[top_genes.index], cmap="viridis")
plt.title("Heatmap of top 20 expressed genes")
plt.tight_layout()
plt.savefig("../figures/top_genes_heatmap.png")
plt.close()
print("Saved figure: figures/top_genes_heatmap.png")

# Histogram of expression values
plt.figure(figsize=(8,6))
plt.hist(expr_df.values.flatten(), bins=50, color='lightgreen')
plt.title("Histogram of normalized gene expression")
plt.xlabel("Expression value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../figures/expression_histogram.png")
plt.close()
print("Saved figure: figures/expression_histogram.png")
