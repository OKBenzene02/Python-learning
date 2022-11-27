import pandas as pd
import numpy as np
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, linear_model

data = pd.read_csv("car.data")
print(data.head())

elements = preprocessing.LabelEncoder()
buying = elements.fit_transform(list(data['buying']))
maint = elements.fit_transform(list(data['maint']))
door = elements.fit_transform(list(data['door']))
persons = elements.fit_transform(list(data['persons']))
lug_boot = elements.fit_transform(list(data['lug_boot']))
safety = elements.fit_transform(list(data['safety']))
class_data = elements.fit_transform(list(data['class']))

predict = "class"

x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(class_data)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
