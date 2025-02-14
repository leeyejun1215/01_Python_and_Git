#1
import pandas as pd

dir = "./data/"
filename = "08_pima-indians-diabetes.data.csv"
filepath = dir + filename

data_columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filepath, names=data_columns)

print(data.head(5))

#2
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
filename = "./data/08_pima-indians-diabetes.data.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv(filename, names=column_names)

array = data.values
print(array, "\n array 변수의 행렬 shape:", array.shape)

#3
X = array[:, 0:8]
print(X, "\nX shape is ", X.shape)
print("-------------------------")
Y = array[:, 8]
print(Y, "\nY shape is ", Y.shape)

#4
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)

print(rescaledX[0:5, :])

#5
import pandas as pd

from sklearn.preprocessing import StandardScaler
filename = "./data/08_pima-indians-diabetes.data.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv(filename, names=column_names)

array = data.values
print(array, "\n array 변수의 행렬 shape:", array.shape)

#6
X = array[:, 0:8]
print(X, "\nX shape is ", X.shape)
print("-------------------------")
Y = array[:, 8]
print(Y, "\nY shape is ", Y.shape)

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
print(rescaledX)

#7
import pandas as pd

from sklearn.preprocessing import Binarizer
filename = "./data/08_pima-indians-diabetes.data.csv"

column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filename, names=column_names)

array = data.values
print(array, "\n array 변수의 형렬 shape:", array.shape)

X = array[:, 0:8]
print(X, "\nX shape is ", X.shape)
print("-------------------------")
Y = array[:, 8]
print(Y, "\nY shape is ", Y.shape)

#8
binarizer = Binarizer(threshold=0.5).fit(X)
binaryX = binarizer.transform(X)

print(binaryX[0:5, :])