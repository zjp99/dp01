# -*- coding: utf-8 -*-#

"""
File         :      tt.py
Description  :  
Author       :      赵金朋
Modify Time  :      2019/5/23 19:02
"""
import numpy as np

# Size of the points dataset.


def error_function(theta, X, y):
    '''Error function J definition.'''
    diff = np.dot(X, theta) - y
    return (1./2*m) * np.dot(np.transpose(diff), diff)

def gradient_function(theta, X, y):
    '''Gradient of the function J definition.'''
    diff = np.dot(X, theta) - y
    return (1./m) * np.dot(np.transpose(X), diff)

def gradient_descent(X, y, alpha):
    '''Perform gradient descent.'''
    theta = np.array([1, 1]).reshape(2, 1)
    print('theta:',theta)
    gradient = gradient_function(theta, X, y)
    print('gradient',gradient)
    while not np.all(np.absolute(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, y)
    return theta

if __name__ == '__main__':
    m = 20
    X0 = np.ones((m, 1))
    X1 = np.arange(1, m+1).reshape(m, 1)
    X = np.hstack((X0, X1))
    y = np.array([
        3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
        11, 13, 13, 16, 17, 18, 17, 19, 21
    ]).reshape(m, 1)

    alpha = 0.01
    print(X)
    print("y:",y)
    optimal = gradient_descent(X, y, alpha)
    print('optimal:', optimal)
    print('error function:', error_function(optimal, X, y)[0,0])