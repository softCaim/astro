import matplotlib.pyplot as plt
import numpy as np
from numpy.random.mtrand import f

k = 3
z = 2
N = 100

x = np.linspace(-10, 10, N)
noise = np.random.normal(0, 2, N)
# noise = np.random.uniform(-3, 3, N)

y = k * x + z


plt.plot(x, y, color="red")

# n = 50
# x_p = np.random.uniform(-10, 10, n)


y_p = y + noise

A = np.array([[N, np.sum(x)], [np.sum(x), np.sum(x**2)]])

B = np.array([np.sum(y_p), np.sum(x * y_p)])

det_1 = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

det_2 = B[1] * A[0, 0] - B[0] * A[1, 0]

det_3 = A[1, 1] * B[0] - A[0, 1] * B[1]

a = det_2 / det_1
b = det_3 / det_1


print(f"a = {a:.2f}, b = {b:.2f}")

l = a * x + b

plt.plot(x, l, color="green")

SSE = np.sum((y_p - np.mean(y_p)) ** 2)
SST = np.sum((y_p - l) ** 2)

r_squared = 1 - (SST / SSE)


plt.scatter(x, y_p)
plt.text(0, 0, f"$r^2$ = {r_squared:.2f}", fontsize=12, color="black")
plt.grid()
plt.show()
