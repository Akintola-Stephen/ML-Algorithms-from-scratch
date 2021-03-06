# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:02:43 2020

@author: AKINTOLA
"""

"""
lr_model is an acronym for "logistic regression model"
n_iter depicts "number of iterations"
lr means "learning rate"
"""
class LogisticRegression:
    
    def __init__(self, lr = 0.001, n_iter = 100 ):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None
        
   """
    X here happens to be a (M * N) dimensional array 
    y happens to be a vector value
    """
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
            
        # Calculating the gradient descent till it gets to the minimum
        for _ in range(self.n_iters):
            lr_model = np.dot(X, self.weights) + self.bias
            y_prediction = self._sigmoid(lr_model)
            
            dw = (1 / n_samples) * np.dot(X.T, (y_prediction - y) )
            db = (1 / n_samples) * np.sum(y_prediction - y)
            
            #Initializing weights and bias with values
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db
    
    
    def predict(self, X):
        lr_model = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(lr_model)
        y_prediction_cls = [ 1 if i > 0.5 else 0 for i in y_predicted ]
        return y_prediction_cls
    
    # A sigmoid function that sets a threshold of 0.5
    def _sigmoid(self, X):
        return 1 / (1 + np.exp(-x))
        
        
        
    
