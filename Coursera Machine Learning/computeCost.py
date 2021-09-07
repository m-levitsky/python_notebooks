import numpy as np

def computeCost(X, y, theta):
    m = len(y)

    # --------------------------
    h = X.dot(theta)
    #---------------------------
    #theta is 2x1, X is 97x2


    
    error = h - y
    #print("error:", error)
    error_sqr = np.square(error)
    #print("error_sqr:", error_sqr)
    J = 1/(2*m) * np.sum(error_sqr)
    #print("J:",J)
    return J
