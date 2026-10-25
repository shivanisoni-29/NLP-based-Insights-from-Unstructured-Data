from datasets import load_dataset

dataset = load_dataset(
    "Tobi-Bueck/customer-support-tickets"
)

df = dataset["train"].to_pandas()

print("Dataset shape :", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())