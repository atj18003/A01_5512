from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

#Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

#Features and target as single DataFrame
df = housing.frame

#Check
print(df.head())
print(df.shape)

#Make boxplot
df.boxplot(rot = 45, figsize=(10,8)).get_figure().savefig("figs/boxplot.png")