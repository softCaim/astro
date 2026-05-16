import matplotlib.pyplot as plt
import numpy as np

A_real = 2
B_real = 0.5

n = 100

x = np.linspace(-10, 10, n)

y = A_real * np.exp(B_real * x)

#noise = np.random.normal(0, 0.3, n)
noise = np.random.uniform(-0.3, 0.3, n)
y_noisy = y + noise
y_noisy = np.clip(y_noisy, 1e-8, None)


K = np.log(y_noisy)

C = np.array([[np.sum(x**2), np.sum(x)], [np.sum(x), n]])

B = np.array([np.sum(K * x), np.sum(K)])

B_i, C_i = np.linalg.solve(C, B)

axal = B_i * x + C_i

A_i = np.exp(C_i)

y_i = A_i * np.exp(B_i * x)

SSE = np.sum((K - np.mean(K)) ** 2)
SST = np.sum((K - axal) ** 2)

r_squared = 1 - (SST / SSE)


plt.plot(x, y, color="green", label="True")

plt.scatter(x, y_noisy, color="red", label="Noise", s=3)

plt.plot(x, y_i, color="blue", label="Fitted", linewidth=5)

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Exponential Function, $r^2$ = {r_squared:.2f}")

plt.legend()
plt.show()
