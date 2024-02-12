import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return x**2 + 2*x -6

x = np.arange(-5, 5, 0.3)

y = funcion(x)

plt.plot(x, y, label='y = x^2 + 2x - 6')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
