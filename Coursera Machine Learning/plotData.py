import matplotlib.pyplot as plt

def plotData(x, y, fig, ax):
    ax.scatter(x=x, y=y, marker='x', c='r', label="Training data")
    ax.set_xlabel('Population of City in 10,000s')
    ax.set_ylabel('Profit in $10,000s')
