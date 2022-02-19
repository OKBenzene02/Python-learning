import pandas as pd
from pandas import DataFrame
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib.pyplot import style

data = pd.read_csv("student-mat.csv", sep=";")
# print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
# print(data.head())

change = "G3"

x = np.array(data.drop([change], 1))
y = np.array(data[change])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

"""best = 0
for i in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    res = linear.score(x_test, y_test)
    print(res)

    if res > best:
        best = res
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
"""

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# Coefficients of linear regression line y = mx + c
print("Coefficient: ", linear.coef_)
print("Intercept: ", linear.intercept_)

predictions = linear.predict(x_test)
# print(len(predictions))

for i in range(len(predictions)):
    print(round(predictions[i]), x_test[i], y_test[i])

p = 'G2'
style.use("ggplot")
pyplot.scatter(data[p], data['G3'])
pyplot.xlabel(p)
pyplot.ylabel("The final grade")
pyplot.show()
