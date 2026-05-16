import numpy as np
import matplotlib.pyplot as plt

A = 2
B = 10

n = 100

x = np.linspace(-9, 10, n)
#x = np.random.normal(1, 10, n)

y = (A*x)/(B+x)

noise = np.random.uniform(-0.9, 0.9, n)
y_noisy = y + noise
z = 1/y_noisy
U = 1/x

C = B/A

G = 1/A

Z = C*U + G

Mat_1 = np.array([[np.sum(U**2),np.sum(U)], [np.sum(U),  n]])

Mat_2 = np.array([np.sum(U*Z), np.sum(Z)])

a, b = np.linalg.solve(Mat_1, Mat_2)

A_dab = 1/b
B_dab = a * A_dab


y_fit = (A_dab * x) / (B_dab + x)

SST = np.sum((y_noisy - np.mean(y_noisy))**2)
SSE = np.sum((y_noisy - y_fit)**2)

r_squared = 1 - SSE / SST

plt.plot(x, y, label='True', color='red', linewidth=2)
plt.scatter(x, y_noisy, color='blue', s=3, label='Noisy')
plt.plot(x, y_fit, color='green', label='Fit')

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"$A$ = {A}, $B$ = {B}, $r^2$ = {r_squared:.2f}, $A_dab$ = {A_dab:.2f}, $B_dab$ = {B_dab:.2f}")
plt.legend()
plt.show()
print(y_fit)
