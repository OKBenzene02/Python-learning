import pandas as pd
from pandas import DataFrame, Series
import numpy as np

missing = np.nan
sr = Series(['Value 1', missing, 'Value 2', missing, 'Value 3', 'Value 5'], name='smtg')
# print(sr.isnull())
# print(sr)

df = DataFrame(np.random.rand(36).reshape(6, 6), index=['row 1','row 2','row 3','row 4','row 5','row 6'],
               columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
# print(df)
df.loc['row 1':'row 5', 'column 1'] = missing
df.loc['row 3':'row 5', 'column 4'] = missing
# print(df)

# to fill nan values with 0
# filled = df.fillna(0)
# print(filled)

# another = df.fillna({'column 1': 23, 'column 4': 45})
# print(another)

# print(df.fillna(method='bfill'))

# Count the missing values
# df.isnull().sum()
# print(df.isnull().sum())

# filter out the missing values
df_no_NaN = df.dropna(axis=1)
print(df_no_NaN)