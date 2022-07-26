import numpy as np
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
sns.set (color_codes=True)


#checking versions of file im working with
print(np.__version__)
print(pd.__version__)
print(sns.__version__)
print (sys.version)

df=pd.read_csv('iris_file.csv')
df.drop("Id", 1, inplace=True)
print(df.columns)
print(df)

print(df["Species"].unique())   # this shows the unique values in the data frame

print(df.info())
print(df.describe())
print(df.groupby("Species").size())


##Data visualization

sns.pairplot(df,ize=3, aspect=1) hue="Species", s
df.hist(edgecolor="red", linewidth=1.2, figsize=(12, 8));
df.boxplot(by="Species", figsize=(12, 8))






