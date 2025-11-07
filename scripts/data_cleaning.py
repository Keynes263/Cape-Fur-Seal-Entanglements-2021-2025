import pandas as pd

# Load dataset
df = pd.read_csv('../data/cape_fur_seal_entanglement_2021-2025.csv')

# Display first few rows
print(df.head())

# Basic summary
print(df.describe())
