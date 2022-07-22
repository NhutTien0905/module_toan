import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron(object):

    '''perceptron classifer
    _ parameters
    eta: float - learning rate (0,1)
    n_iter: int - passes over training dataset
    
    _ attributes
    w_ : 1d array - weight after fitting
    errors: list - number of misclassification each epoch'''

    def __init__(self,eta = 0.01,n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(seft,X,y):

        '''fit training
        _ parameters
        X: {array-like} shape = [n_samples,n_feature]
            training vector where n_samples is the number of samples,
            n_feature is the number of features
        y: {array_like} shape = [n_samples]
            target values
        
        return
        --------
        seft: object'''

        # shape[1] là số cột
        seft.w_ = np.zeros(1+X.shape[1]) 
        seft.errors_ = []

        for _ in range(seft.n_iter):
            errors = 0
            # zip(...) dùng để gộp 2 mảng
            # dòng này là gọi từng phàn tử tương ứng của 2 mảng
            for xi, target in zip(X,y):
                update = seft.eta * (target - seft.predict(xi))
                seft.w_[1:] += update * xi
                seft.w_[0] += update
                errors += int(update != 0.0)
            seft.errors_.append(errors)
        return seft

    def net_input(seft,X):
        # calculate the net input
        return np.dot(X,seft.w_[1:]) + seft.w_[0]

    def predict(seft,X):
        # return class label after unit step
        return np.where(seft.net_input(X)>=0,1,-1) 

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
df.tail()

# lấy giá trị 100 hàng đầu cột 4
y = df.iloc[0:99,4].values
# setosa thì -1 mấy kia là 1
y = np.where(y == 'Iris-setosa',-1,1)
# lấy giá trị 100 hàng đầu cột 0, 2
X = df.iloc[0:99,[0,2]].values

# vẽ đồ thị phân loại
plt.scatter(X[:49,0],X[:49,1],color = 'red',marker = 'o', label = 'setosa')
plt.scatter(X[49:100,0],X[49:100,1], color = 'blue',marker = 'x',label = 'versicolor')
plt.xlabel('Pental length')
plt.ylabel('Sepal length')
plt.legend(loc = 'upper left')
plt.show()

# vẽ số phân loại sai mỗi kỳ
ppn = Perceptron(eta=0.1,n_iter=10)
ppn.fit(X,y)
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker = 'o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()