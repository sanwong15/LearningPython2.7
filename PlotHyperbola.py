# San Wong hswong1@uci.edu

# An example from Math
# Plotting a hyperbola in the unit interval Needs a loop.
# Invariant given is the product of x an y is k

import matplotlib.pyplot as plt
import numpy as np

def Hyperbola (a,b):
    x1 = np.arange(0, 1000, 0.01)
    y1 = [a / (b - i) for i in x1]
    plt.plot(x1, y1, 'r')
    plt.axis([0, 1000, -10, 10])

    plt.show()

Hyperbola(10,500)