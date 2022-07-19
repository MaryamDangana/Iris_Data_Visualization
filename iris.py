#iris dataset was obtained from UCI machine learning repository  link--https://archive.ics.uci.edu/ml/datasets/Iris/
#The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor)
# . Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
# Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species
# from each other.
#importing useful libraries


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

display(sns.pairplot(df, hue="Species", size=3, aspect=1))





