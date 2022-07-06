import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from matplotlib import rcParams

# %matplotlib inline
rcParams['figure.figsize'] = 5, 4

x = range(1, 10)
y = [4, 3, 2, 1, 0, 1, 2, 3, 4]

fig = plt.figure()
ax = fig.add_axes([.1, .1, .1, .1])
ax.plot(x, y)
plt.show()