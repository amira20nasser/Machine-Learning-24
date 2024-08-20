import itertools
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn import preprocessing, metrics
from sklearn import linear_model
from sklearn.model_selection import train_test_split


class Polynomial:
    def __init__(self, degree):
        self.degree = degree

    def transform(self, X):
        n_samples, n_features = X.shape
        combinations = self._combinations(n_features)
        # print(combinations)
        n_output_features = len(combinations)
        result = np.empty((n_samples, n_output_features))
        for i, comb in enumerate(combinations):
            # column i
            result[:, i] = np.prod(X[:, comb], axis=1)
        return np.hstack([np.ones((n_samples, 1)), result])

    def _combinations(self, n_features):
        combinations = []
        for d in range(1, self.degree + 1):
            for c in itertools.combinations_with_replacement(range(n_features), d):
                combinations.append(c)
        return combinations


data = pd.read_csv("assignment2dataset.csv")
print(data.dtypes)
# preprocessing
print("\n\t\t*****Number of nulls******")
print(data.isnull().sum())
print("\n\t\t*****Duplicated Data******")
print(data.duplicated().sum())
data.drop_duplicates(inplace=True)

# implement labelEncoding
le = preprocessing.LabelEncoder()
data["Extracurricular Activities"] = le.fit_transform(data["Extracurricular Activities"])
print("\n\t\t*****AFTER PREPROCESSING******")
print(data.dtypes)

# Feature Selection
corr = data.corr()
print(corr)
# select 2 column
# top_feature = corr.index[abs(corr['Performance Index']) >= 0.30]
# select 4 column
top_feature = corr.index[abs(corr['Performance Index']) >= 0.03]
plt.subplots(figsize=(50, 10))
top_corr = data[top_feature].corr()
sns.heatmap(top_corr, cmap=plt.cm.CMRmap_r,annot=True)
plt.show()
top_feature = top_feature.delete(-1)

X = data[top_feature]
Y = data['Performance Index']

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.8,test_size=0.2,random_state=42)
# CONVERT TO ARRAY
X_train_arr = X_train.to_numpy()
X_test_arr = X_test.to_numpy()

# TRAINING DATA
polymial = Polynomial(2)
X_train_poly = polymial.transform(X_train_arr)
poly_model = linear_model.LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_train_predicted = poly_model.predict(X_train_poly)
print(f"intercept: {poly_model.intercept_}")
print(f"coefficients: {poly_model.coef_}")
print('Mean Square Error for Train Data', metrics.mean_squared_error(y_train, y_train_predicted))

# Test DATA
X_test_poly = polymial.transform(X_test_arr)
y_test_predicted = poly_model.predict(X_test_poly)
print('Mean Square Error For TEST', metrics.mean_squared_error(y_test, y_test_predicted))
