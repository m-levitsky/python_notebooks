import numpy as np
import computeCost as cc

def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros([num_iters,1])

    for iter in range(num_iters):

        h = X.dot(theta)
        errors = h - y


        theta_change = (alpha/m) * (X.transpose().dot(errors))
        theta = theta - theta_change

        J_history[iter] = cc.computeCost(X, y, theta)

    return theta
