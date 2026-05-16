import numpy as np
import matplotlib.pyplot as plt

n = 500
l = int(n**(1/2))
x = np.random.uniform(-5, 5, n)
"""plt.scatter(np.linspace(0, n, n), x)
plt.show()
plt.hist(x, bins=l, edgecolor='black')
plt.title("Histogram")
plt.show()"""

y = np.random.normal(4, 1, n)

plt.scatter(np.linspace(0, n, n), y)
plt.show()
plt.hist(y, bins=l, edgecolor='black')
plt.title("Histogram")
plt.show()
