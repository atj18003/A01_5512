from scikit.databases import fetch_california_housing
import pandas as pd

#Load California Housing dataset
housing = fetch_california_housing(as_frame = True)

#Features and target as single DataFrame
df = housing.frame

#Check
print(df.head())
print(df.shape)