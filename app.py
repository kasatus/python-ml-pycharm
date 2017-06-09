import numpy as np
import pandas

#print(np.array([3, 4, True]))
train = pandas.read_csv("train.csv")
test = pandas.read_csv("test.csv")
# print(train.head())
#print(train.describe())
# print(train.shape)
#print(train["Survived"].value_counts())
print(train["Survived"].value_counts(normalize = True))