import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from matplotlib import rcParams

# Plotting a line chart in matplotlib
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]
#
# plt.plot(x, y)
# plt.show()

# Line chart using Pandas object
cars = pd.read_csv('mtcars.csv')
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']
# mpg.plot()
# plt.show()

# Line chart using three variables
# df = cars[['mpg', 'cyl', 'wt']]
# df.plot()
# plt.show()

# Bar Chart
# plt.bar(x, y)
# plt.show()

# Creating Bar chart using Pandas object
# mpg.plot(kind='bar') # this shows the vertical bar chart data
# mpg.plot(kind="barh") # this shows the horizontal bar chart data
# plt.show()

# Creating Pie charts
pie = [1, 2, 3, 4, 0.5, 0.9]
# plt.pie(pie)
# plt.show()

# Saving a plot
# plt.plot(mpg)
# plt.savefig('examplePlot.png')
# plt.show()