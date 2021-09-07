import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warmUpExercise as wue
import plotData as plot
import computeCost as cc
import gradientDescent as gd




# ==================== Part 1: Basic Function ====================

print("Running warmUpExercise ... \n")
print("5x5 identity matrix: \n")
wue.warmUpExercise()

input("Program paused. Press enter to continue. \n")

# ======================= Part 2: Plotting =======================

print("Plotting Data ... \n")


data = pd.read_csv('ex1data1.txt', header = None)
X = data.iloc[:,0]
y = data.iloc[:,1]
m = len(y)
data.head()

fig, ax = plt.subplots()
plot.plotData(X, y, fig, ax)


input("Program paused. Press enter to continue. \n")

# =================== Part 3: Cost and Gradient descent ===================



X = X[:,np.newaxis]
y = y[:,np.newaxis]

ones = np.ones((m,1))
X = np.hstack((ones, X))

theta = np.zeros([2,1])
print(theta)

iterations = 1500
alpha = 0.01

print("\nTesting the cost function ...\n")

J = cc.computeCost(X, y, theta)

print("With theta = [0 ; 0]\nCost computed = \n", J)
print("Expected cost value (approx) 32.07\n")

theta_2 = np.array([[-1],[2]])
print(theta_2)

J = cc.computeCost(X, y, theta_2)

print("\nWith theta = [-1 ; 2]\nCost computed = \n", J)
print("Expected cost value (approx) 54.24\n")

input("Program paused. Press enter to continue. \n")

print("\nRunning Gradient Descent ...\n")

theta = gd.gradientDescent(X, y, theta, alpha, iterations)

print("Theta found by gradient descent:\n", theta)
print("Expected theta values (approx)\n")
print(" -3.6303\n  1.1664\n\n")





ax.plot(X[:,1], X.dot(theta), label="Linear regression")
plt.legend()
plt.show()
