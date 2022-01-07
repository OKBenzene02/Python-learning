import pandas as pd
import numpy as np
import sklearn

data = pd.read_csv("student-mat.csv", sep=";")
# print(data.head())

data = data[["G1", "G2", "G3", "school", "sex"]]
# print(data.head())

change = "G3"

x = np.array(data.drop([change], 1))
y = np.array(data[change])

x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

print(x_train)
print(y_train)
print(x_test)
print(y_test)