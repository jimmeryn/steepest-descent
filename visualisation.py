import numpy as np
import matplotlib.pyplot as plt


def visualisation(fun, size):
    x = np.linspace(-size, size, 100)
    y = np.linspace(-size, size, 100)
    X, Y = np.meshgrid(x, y)
    Z = fun(X, Y)
    plt.contourf(X, Y, Z, 20, cmap="RdYlGn")
    plt.colorbar()
    plt.show()
