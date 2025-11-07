import pandas as pd

# Load dataset
df = pd.read_xlsx('../data/cape_fur_seal_entanglement_2021_2025.xlsx')

# Display first few rows
print(df.head())

# Basic summary
print(df.describe())
