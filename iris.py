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




