import matplotlib.pyplot as plt
import numpy as np
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
plt.imshow(gardamavali_sin, cmap="gray", vmin=0, vmax=1)
plt.axis("on")
plt.show()

row = 50

vertical_sin = gardamavali_sin[row, :]

plt.plot(vertical_sin, color="blue")
plt.ylim(0, 1)
plt.show()
