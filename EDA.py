# ====== Exploratory Data Analysis on Titanic Dataset ======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset load karna
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 1. Dataset ka basic info
print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nData Types:\n", df.dtypes)

# 2. Missing values check
print("\nMissing Values:\n", df.isnull().sum())

# 3. Summary statistics
print("\nSummary Statistics:\n", df.describe())

# 4. Gender distribution
sns.countplot(x='Sex', data=df)
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")
plt.show()

# 5. Survival count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.savefig("survival_count.png")
plt.show()

# 6. Age distribution
sns.histplot(df['Age'].dropna(), bins=20, kde=True)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.show()

# 7. Correlation heatmap (only numeric columns)
plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# Save cleaned data
df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned data saved as titanic_cleaned.csv")