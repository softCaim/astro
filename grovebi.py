import matplotlib.pyplot as plt
import numpy as np

data = []

header = ["x", "y", "V_x", "V_y", "V_z"]

with open("grova1.csv", "r") as f:
    for line in f:
        row = [float(v) for v in line.strip().split(",")]
        data.append(row)

data = np.array(data)

print(header)
print(data)
print("Number of points:", len(data))

X = data[:, 0]
Y = data[:, 1]

v_1 = data[:, 2]
v_2 = data[:, 3]
v_3 = data[:, 4]

n = len(data)

plt.figure()
plt.scatter(X, Y, color="red", s=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Particle positions")
plt.axis("equal")
plt.show()

plt.figure()
plt.scatter(v_1, v_2, color="blue", s=1)
plt.xlabel("V_x")
plt.ylabel("V_y")
plt.title("Velocity space")
plt.axis("equal")
plt.show()

v_abs = np.sqrt(v_1**2 + v_2**2 + v_3**2)
filt = np.where(v_abs > 4)[0]

print("Filtered particles:", len(filt))

x_min, x_max = 4.0, 6.0

plt.figure()
plt.hist(v_1, bins=int(np.sqrt(n)), density=True, edgecolor="black")

mask = (v_1 >= x_min) & (v_1 <= x_max)
mu, sigma = norm.fit(v_1[mask])

x_fit = np.linspace(x_min, x_max, 200)

plt.plot(
    x_fit,
    norm.pdf(x_fit, mu, sigma),
    "r-",
    linewidth=2,
    label=f"N(μ={mu:.2f}, σ={sigma:.2f})",
)

plt.xlabel("V_x")
plt.ylabel("density")
plt.title("Gaussian fit for V_x")
plt.legend()
plt.show()

print(f"N(μ={mu:.2f}, σ={sigma:.2f})")

plt.figure()
plt.hist(X, bins=int(np.sqrt(n)), density=True, edgecolor="black")
plt.title("Distribution of X")
plt.xlabel("X")
plt.ylabel("density")
plt.show()

plt.figure()
plt.hist(Y, bins=int(np.sqrt(n)), density=True, edgecolor="black")
plt.title("Distribution of Y")
plt.xlabel("Y")
plt.ylabel("density")
plt.show()

mask = (X >= 15) & (X <= 25) & (Y >= 7) & (Y <= 15)

X_sel = X[mask]
Y_sel = Y[mask]

x_c = np.mean(X_sel)
y_c = np.mean(Y_sel)


r = np.sqrt((X_sel - x_c) ** 2 + (Y_sel - y_c) ** 2)
R = np.max(r)

N_bins = 5
r1 = R / np.sqrt(N_bins)
n_array = np.arange(N_bins + 1)
r_min = 0.5 * r1
bins = r_min + (R - r_min) * np.sqrt(n_array / N_bins)

t = np.linspace(0, 2 * np.pi, 500)

plt.figure()

plt.scatter(X, Y, color="lightgray", s=1)

plt.scatter(X_sel, Y_sel, color="red", s=1)

for radius in bins:
    x_circle = x_c + radius * np.cos(t)
    y_circle = y_c + radius * np.sin(t)
    plt.plot(x_circle, y_circle, color="black", alpha=0.3)

plt.scatter([x_c], [y_c], color="red", s=20)

plt.title("Particles with radial bins")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()

counts, edges = np.histogram(r, bins=bins)

r_mid = 0.5 * (edges[:-1] + edges[1:])

plt.figure()
plt.plot(r_mid, counts, linewidth=2)
plt.title("Radial density (equal-area rings)")
plt.xlabel("r")
plt.ylabel("number of particles")
plt.grid()
plt.show()
