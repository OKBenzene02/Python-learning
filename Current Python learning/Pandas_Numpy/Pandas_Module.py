import pandas as pd
from pandas import DataFrame, Series
import numpy as np

"""Example of Data Frame"""
# df = pd.DataFrame({"Column-1" : ["row1 col1", "row1 col2"],
#                    "Column-2": ["row2 col1", "row2 col2"]})
#
# print(df)

# Adding new columns and rows
# df = pd.DataFrame([[1, 2], [3, 4]], index=["ind-1", "ind-2"], columns=["col1", "col2"])
# df["col3"] = [5, 6] # adding new column
# print(df)

# df = pd.DataFrame([[1, 2], [3, 4]], index=["ind-1", "ind-2"], columns=["col1", "col2"])
# df1 = pd.DataFrame([[5, 6], [7, 8]], index=["ind-3", "ind-4"], columns=["col1", "col2"])
# print(df.append(df1)) # Adding new row using another dataframe

"""Example of Series"""
# sr = pd.Series([1, "Hello", 3, "3324 str"], index=["ind-1", "ind-2", "ind-3", "ind-4"], name="Example of series")
# print(sr)

"""Data Access Methods"""
# data = pd.read_csv("students.csv")
# head method to print first 5 rows
# print(data.head())

# tail method to print last 5 rows
# print(data.tail())

# Accessing complete column
# print(data["First Name"])
# print(data["Email ID"])

# print(data)

"""Randomly arranging data"""

sr = Series(np.arange(8), index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8'])
# print(sr)

# accessing data
# print(sr['row 5'])

# accessing rows
# print(sr[[4, 5]])

df = DataFrame(np.random.rand(36).reshape(6, 6), index=['row 1','row 2','row 3','row 4','row 5','row 6'],
               columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
# print(df)

# print(df.loc[['row 1', 'row 2', 'row 3'], ['column 1', 'column 2', 'column 3']])

# Data slicing
# print(sr['row 1':'row 5'])

# Comparing with scalars
# print(df > .2)

# filtering with scalars
# print(df[df > .2])
# print(sr[sr < 3])

# setting the values with scalars
