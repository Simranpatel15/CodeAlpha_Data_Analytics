import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

print(df.head())

# 1. Count plot of species
sns.countplot(x="species", data=df)
plt.title("Number of Samples per Species")
plt.savefig("species_count.png")
plt.show()

# 2. Scatter plot: sepal_length vs sepal_width
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df)
plt.title("Sepal Length vs Width")
plt.savefig("sepal_scatter.png")
plt.show()

# 3. Pairplot for all features
sns.pairplot(df, hue="species")
plt.savefig("pairplot.png")
plt.show()

# 4. Boxplot of petal_length by species
sns.boxplot(x="species", y="petal_length", data=df)
plt.title("Petal Length by Species")
plt.savefig("petal_boxplot.png")
plt.show()