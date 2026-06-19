import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from skimage.measure import profile_line

"""x = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(x)

plt.imshow(x, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

y = []
for i in range(3):
    for k in range(3):
        y.append(0)

y = np.array(y).reshape(3, 3)


print(y)

plt.imshow(y, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


v = []
for i in range(3):
    for l in range(3):
        v.append(0)

matrix = []
x = v[0:3]
o = v[3:6]
z = v[6:9]

for i in x, o, z:
    matrix.append(i)

for row in matrix:
    print(row)


f = np.ones((20, 10))
# print(f)

plt.imshow(f, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

black = np.zeros((20, 10))

plt.imshow(black, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


j = np.ones((20, 20))

for i in range(20):
    for k in range(20):
        if k == 10:
            j[i, k] = 0

print(j)

plt.imshow(j, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

black_white = np.zeros((20, 20))

for i in range(20):
    for k in range(20):
        if k == 10:
            black_white[i, k] = 1


print(black_white)

plt.imshow(black_white, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


white_black = []

for i in range(10):
    for k in range(9):
        if i == 4:
            white_black.append(0)
        else:
            white_black.append(1)


white_black = np.array(white_black).reshape(10, 9)

print(white_black)

plt.imshow(white_black, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


tetri_horizont = np.zeros((10, 9))

for i in range(10):
    for k in range(9):
        if i == 4:
            tetri_horizont[i, k] = 1


print(tetri_horizont)

plt.imshow(tetri_horizont, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


shavi_djvari = np.ones((10, 10))

for i in range(10):
    for k in range(10):
        if i == 4 or k == 4:
            shavi_djvari[i, k] = 0

# print(shavi_djvari)

plt.imshow(shavi_djvari, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


tetri_djvari = np.zeros((10, 10))

for i in range(10):
    for k in range(10):
        if i == 4 or k == 4:
            tetri_djvari[i, k] = 1

# print(tetri_djvari)

plt.imshow(tetri_djvari, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


diagonaluri_djvari_shav_fonze = np.zeros((10, 10))

w = 9
for i in range(10):
    for k in range(10):
        if i == k:
            diagonaluri_djvari_shav_fonze[i, k] = 1

        if i == 9 - w and k == w:  # შესაძლოა if i + k == 9 იც
            diagonaluri_djvari_shav_fonze[i, k] = 1

            print(w)

            w -= 1

print(diagonaluri_djvari_shav_fonze)

plt.imshow(diagonaluri_djvari_shav_fonze, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


shavi = np.ones((10, 10))
tetri = np.zeros((10, 10))

dajameba = np.concatenate((shavi, tetri), axis=1)

print(dajameba)

plt.imshow(dajameba, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


dafa = np.ones((8, 8))

for i in range(8):
    for k in range(8):
        if k % 2 != 0 and i % 2 == 0:
            dafa[i, k] = 0
        if k % 2 == 0 and i % 2 != 0:
            dafa[i, k] = 0

print(dafa)

plt.imshow(dafa, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

"""
gardamavali = np.zeros((11, 11))

for i in range(11):
    for k in range(11):
        if k != 0:
            gardamavali[i, k] = k * 0.1


print(gardamavali)

plt.imshow(gardamavali, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

gardamavali2 = np.zeros((11, 11))

for i in range(11):
    for k in range(11):
        if i != 0:
            gardamavali2[i, k] = i * 0.1

print(gardamavali2)

plt.imshow(gardamavali2, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


row = 5
col = 5

horizontal_profile = profile_line(gardamavali, (row, 0), (row, 10))
vertical_profile = profile_line(gardamavali, (0, col), (10, col))

plt.plot(horizontal_profile, color="red")
plt.ylim(0, 1)
plt.show()

plt.plot(vertical_profile, color="blue")
plt.ylim(0, 1)
plt.show()


gardamavali_sin = np.zeros((100, 100))

for i in range(100):
    for k in range(100):
        gardamavali_sin[i, k] = (np.sin(k * 0.1) + 1) / 2
print("sin")
print(gardamavali_sin)
plt.imshow(gardamavali_sin, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

row = 50

vertical_sin = gardamavali_sin[row, :]

plt.plot(vertical_sin, color="blue")
plt.ylim(0, 1)
plt.show()

x = np.arange(
    len(vertical_sin)
)  # ქმნის ჰორიზონტალზე წერტილებს მათი ნომრების ასაღებად, თუ vertical_sin ში მნიშვნელობაა, მაშინ x იქნება 0,..,99, ანუ პროფილის ყველა წერტილს თავისი ნომერი აქვს


def sin_model(x, a, b, c, d):
    return (
        a * np.sin(b * x + c) + d
    )  # სინუსოიდას აღწერა, a - ამპლიტუდა, b - სიხშირე(რამდენად მეორდება ტალღა), c - ფაზური გაწევა(ტალღა მარჯვნივ იწევა თუ მარცხნივ), d - ვერტიკალური გაწევა(ზემოთ რამდენად არის ზემოთ)


params, covariance = curve_fit(
    sin_model, x, vertical_sin, p0=[0.5, 0.1, 0, 0.5]
)  # curve_fit იღებს სინუსსს, წერტილების კოორდინატებს და პროფილის რეალურ მნიშვნელობებს და უსადაგებს a, b, c, d პარამეტრებს ისე რომ ფორმულა იყოს მაქსიმალურად ახლო რეალურ მონაცემებთან
# params = [a, b, c, d] covariance - ინფორმაცია პარამეტრების სიზუსტეზე
fit = sin_model(
    x, *params
)  # ნაპოვნი მონაცემების მიხედვით მოდელის ფიტის გამოთვლა, თუ params = [0.5, 0.1, 0, 0.1], მაშინ ეს იგივე იქნება რაც sin_model(x, 0.5, 0.1, 0, 0.1)

plt.plot(
    x, vertical_sin, color="blue", label="profile"
)  # თავდაპირველ პროფილს ლურჯად ხატავს
plt.plot(
    x, fit, color="red", linestyle="--", label="fit"
)  # ნაპოვნ ფიტს წითელი წყვეტილი ხაზებით ხატავს
plt.ylim(0, 1)
plt.legend()
plt.show()

print(params)


print("----------------------------\n უფრო მაღალი ტონალობები ექსპონენტით")

gardamavali_exp = np.zeros((100, 100))

for i in range(100):
    for j in range(100):
        gardamavali_exp[i, j] = np.exp(j / 99)

max_value = np.max(gardamavali_exp)
min_value = np.min(gardamavali_exp)

gardamavali_new = (gardamavali_exp - min_value) / (max_value - min_value)

print(gardamavali_new)

plt.imshow(gardamavali_new, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

profile = gardamavali_new[row, :]
plt.plot(profile, label="profile")
plt.ylim(0, 1)
plt.show()

x_exp = np.arange(len(profile))


def exp_model(x, a, b, c):
    return a * np.exp(b * x) + c


params, covariance = curve_fit(exp_model, x, profile, p0=[0.01, 0.05, 0])

fit = exp_model(x, *params)

plt.plot(x, profile, label="profile")
plt.plot(x, fit, color="red", linestyle="--", label="fit")
plt.ylim(0, 1)
plt.show()

print("----------------------------\n გაუსი")


tonaloba = np.zeros((100, 100))


k = np.linspace(-5, 5, 100)

y = np.exp(-1 * ((k - 1) / 2) ** 2)
plt.plot(k, y)
plt.show()

for i in range(100):
    for j in range(100):
        tonaloba[i, j] = y[j]

max_value = np.max(tonaloba)
min_value = np.min(tonaloba)

tonaloba_new = (tonaloba - min_value) / (max_value - min_value)

print(tonaloba_new)

plt.imshow(tonaloba_new, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()


profile = tonaloba_new[row, :]

plt.plot(profile, label="profile")
plt.ylim(0, 1)
plt.show()


def gaussian(k, a):
    return a * (np.exp(-(((k - 1) / 2) ** 2)))


params, covariance = curve_fit(gaussian, k, profile, p0=[0])

fit = gaussian(k, *params)

plt.plot(k, profile, label="profile")
plt.plot(k, fit, color="red", linestyle="--", label="fit")
plt.ylim(0, 1)
plt.show()


print("----------------------------\n ლაპლასი")

l = np.linspace(-5, 5, 100)

mod = np.abs(l - 1)

laplace = 0.5 * np.exp(-(mod / 2))

plt.plot(l, laplace)
plt.show()

for i in range(100):
    for j in range(100):
        tonaloba[i, j] = laplace[j]

max_value = np.max(tonaloba)
min_value = np.min(tonaloba)

tonaloba_new = (tonaloba - min_value) / (max_value - min_value)

print(tonaloba_new)

plt.imshow(tonaloba_new, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

profile = tonaloba_new[row, :]

plt.plot(profile, label="profile")
plt.ylim(0, 1)
plt.show()


def laplace_func(mod, a, b):
    return a * np.exp(-(mod / b))


params, covariance = curve_fit(laplace_func, mod, profile, p0=[1, 2])

fit = laplace_func(mod, *params)

plt.plot(l, profile, label="profile")
plt.plot(l, fit, color="red", linestyle="--", label="fit")
plt.ylim(0, 1)
plt.show()
