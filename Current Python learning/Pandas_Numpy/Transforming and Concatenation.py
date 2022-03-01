import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df = DataFrame(np.arange(36).reshape(6, 6))
# print(df)

df1 = DataFrame(np.arange(15).reshape(5, 3))
# print(df1)

# Concatenation
# print(pd.concat([df, df1], axis=1))

# Transforming data
# drop
# print(df.drop([0, 2])) # drop rows
# print(df.drop([0, 2], axis=1)) # drop columns

# adding data
sr = Series(np.arange(6), name="New")
# print(sr)
added_data = DataFrame.join(df, sr)
# print(added_data)

# new_table = added_data.append(added_data, ignore_index=False) # this will repeat data
# print(new_table)

new_table = added_data.append(added_data, ignore_index=True) # Renames the columns
# print(new_table)

sorting = df.sort_values(by=(5), ascending=[False])
print(sorting)