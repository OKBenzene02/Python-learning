import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df = DataFrame({
    'Column 1': [1, 1, 2, 2, 3, 3, 3],
    'Column 2': ["a", "a", "b", "b", "c", 'c', 'c'],
    'Column 3': ['A', "A", 'B', 'B', "C", "D", "C"]
})

print(df)
print(df.duplicated())
# print(df.drop_duplicates())
print(df.drop_duplicates(['Column 3']))