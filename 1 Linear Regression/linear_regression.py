import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

# Loading data
data = pd.read_csv('assignment1dataset.csv')
# print("DESCRIBE DATA")
# print(data.describe())
# print("SAMPLE FROM DATA")
# print(data.head())
Y = data['Performance Index']


class GradientDescent:
    @staticmethod
    def calc_gradient_descent(X, Y, m, c, epochs, L):
        n = len(X)
        for i in range(epochs):
            y_prediction = m * X + c
            d_m = (-2 / n) * sum((Y - y_prediction) * X)
            d_c = (-2 / n) * sum(Y - y_prediction)
            m = m - L * d_m
            c = c - L * d_c
        return m, c


class Model:
    @staticmethod
    def calc_feature(X, Y, m, c, L, epochs, name_col):
        m, c = GradientDescent.calc_gradient_descent(X, Y, m, c, epochs, L)
        prediction = m * X + c
        plt.scatter(X, Y,c="grey")
        plt.xlabel(name_col, fontsize=20)
        plt.plot(X, prediction, color='pink', linewidth=2)
        plt.show()
        print('Mean Square Error ', name_col+ ' : '+ str(metrics.mean_squared_error(Y, prediction)))


Model().calc_feature(data['Previous Scores'],Y,800,0,0.0001,70,'Previous Scores')
Model().calc_feature(data['Sleep Hours'], Y, 80, 0, 0.01, 900,'Sleep Hours')
Model().calc_feature(data['Hours Studied'], Y, 80, 0, 0.01, 900,'Hours Studied')
Model().calc_feature(data['Sample Question Papers Practiced'], Y, 40, 0, 0.01, 800,'Sample Question Papers Practiced')


# Model().calc_feature(pd.DataFrame(data['Hours Studied'] + data['Previous Scores']), Y, 1000, 0.1, 0.01, 20,'scores / hours')
