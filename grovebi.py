import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

data = []  # ცარიელი სიაა, სადაც შეინახება მონაცემები ფაილებიდან

header = ["x", "y", "V_x", "V_y", "V_z"]  # სვეტების დასათეურება

with open(
    "grova1.csv", "r"
) as f:  # ვხსნი ფაილს წასაკითხად და with ის საშუალებით წაკითხვის მერე ეგრევე დახურავს
    for line in f:  # ფაილის ყველა ხაზს მიყვება
        row = [
            float(v) for v in line.strip().split(",")
        ]  # line.strip() - სფეისების ხსნის, split(",") - სტრიქონებს , ით ყოფს, float(v) - თითოეული სვეტის მნიშვნელობას გადააქცევს რიცხვად(ანუ საბოლოოდ მიიღება რიცხვების ლისტს ერთ სტრიქონში)
        data.append(row)  # row - ს ამატებს data ლისტში

data = np.array(data)  # data ლისტს გადააქცევს numpy მასივად

print(header)  # სვეტების სახელების დაბეჭდვა
print(data)  # ყველა მნიშვნელობის დაბეჭდვა
print("Number of points:", len(data))  # სტრიქონების - ვარსკვლავების რაოდენობა

X = data[
    :, 0
]  # X - ვიღებს ყველა სტრქონს და ვუსაბამებ კოორდინატს სვეტიდან (0 სვეტი - X კოორდინატი)
Y = data[
    :, 1
]  # Y - ვიღებს ყველა სტრქონს და ვუსაბამებ კოორდინატს სვეტიდან (1 სვეტი - Y კოორდინატი)
v_1 = data[
    :, 2
]  # v_1 - ვიღებს ყველა სტრქონს და ვუსაბამებ კოორდინატს სვეტიდან (2 სვეტი - v_1 კოორდინატი)
v_2 = data[
    :, 3
]  # v_2 - ვიღებს ყველა სტრქონს და ვუსაბამებ კოორდინატს სვეტიდან (3 სვეტი - v_2 კოორდინატი)
v_3 = data[
    :, 4
]  # v_3 - ვიღებს ყველა სტრქონს და ვუსაბამებ კოორდინატს სვეტიდან (4 სვეტი - v_3 კოორდინატი)

n = len(data)  # ვარსკვლავების რაოდენობა

plt.figure()  # ვქმნის ახალ ფანჯარას გრაფიკისთვის
plt.scatter(
    X, Y, color="red", s=1
)  # ვსვამ წერტილებს X და Y კოორდინატებზე, s = 1 წერტილის ზომა
plt.xlabel("x")  # X კოორდინატის სათაური
plt.ylabel("y")  # Y კოორდინატის სათაური
plt.title("Particle positions")  # გრაფიკის სათაური
plt.axis("equal")  # X და Y კოორდინატების სიდიდე-მაშტაბი ერთნაირია
plt.show()  # გრაფიკის ჩვენება

plt.figure()
plt.scatter(
    v_1, v_2, color="blue", s=1
)  # V_x და V_y კოორდინატების-სიჩქარეების სიბრტყე, s=1 სიდიდე-მაშტაბი ერთნაირია
plt.xlabel("V_x")  # V_x კოორდინატის სათაური
plt.ylabel("V_y")  # V_y კოორდინატის სათაური
plt.title("Velocity space")
plt.axis("equal")
plt.show()

v_abs = np.sqrt(
    v_1**2 + v_2**2 + v_3**2
)  # აბსოლუტური სიჩქარე(სიჩქარის მოდული), ანუ სიჩქარეების კვადრატების ჯამიდან ფესვი
filt = np.where(v_abs > 4)[
    0
]  # ვეძებ იმ ვარსკვლავები სიჩქარეს, რომლების სიჩქარეც მეტია 4-ზე

print("Filtered particles:", len(filt))  # ვპრინტავთ გაფილტრულ ვარსკვლავების რაოდენობას


# ჰისტოგრამა V_x კოორდინატის სიჩქარეების განაწილებისთვის
x_min, x_max = 4.0, 6.0  # მონაცემების ამორჩევის დიაპაზონი

plt.figure()
plt.hist(
    v_1, bins=int(np.sqrt(n)), density=True, edgecolor="black"
)  # ჰისტოგრამა V_x კოორდინატის სიჩქარეების განაწილებისთვის

mask = (v_1 >= x_min) & (v_1 <= x_max)  # V_x მნიშვნელობების ფილტრი [4,6] დიაპაზონში
mu, sigma = norm.fit(
    v_1[mask]
)  # mu - საშუალო, sigma - სტანდარტული გადახრა (მომზადება სტანდარტული გადახრისთვის)

x_fit = np.linspace(x_min, x_max, 200)  # ფუნქციის გრაფიკისთვის ბადის აგება

plt.plot(
    x_fit,
    norm.pdf(x_fit, mu, sigma),
    "r-",
    linewidth=2,
    label=f"N(μ={mu:.2f}, σ={sigma:.2f})",
)  # ჰისტოგრამის ზემოთ ვაგებთ გაუსიანას

plt.xlabel("V_x")
plt.ylabel("density")
plt.title("Gaussian fit for V_x")
plt.legend()
plt.show()

print(f"N(μ={mu:.2f}, σ={sigma:.2f})")  # პარამეტრების განაწილების ბეჭდვა

plt.figure()
plt.hist(X, bins=int(np.sqrt(n)), density=True, edgecolor="black")  # X ის განაწილება
plt.title("Distribution of X")
plt.xlabel("X")
plt.ylabel("density")
plt.show()

plt.figure()
plt.hist(Y, bins=int(np.sqrt(n)), density=True, edgecolor="black")  # Y ის განაწილება
plt.title("Distribution of Y")
plt.xlabel("Y")
plt.ylabel("density")
plt.show()

mask = (
    (X >= 15) & (X <= 25) & (Y >= 7) & (Y <= 15)
)  # X და Y კოორდინატებიდან ვიღებ მხოლოდ მართკუთხა მიდამოდან

X_sel = X[mask]  # ვიყენებ ფილტრს
Y_sel = Y[mask]  # ვიყენებ ფილტრს

x_c = np.mean(
    X_sel
)  # X კოორდინატების საშუალო (არჩეული წერტილების მასების ცენტს ვითვლით)
y_c = np.mean(
    Y_sel
)  # Y კოორდინატების საშუალო (არჩეული წერტილების მასების ცენტს ვითვლით)


r = np.sqrt(
    (X_sel - x_c) ** 2 + (Y_sel - y_c) ** 2
)  # ყოველი წერტილის მანძილი ცენტრიდან
R = np.max(r)  # მაქსიმალური რადიუსი

N_bins = 5  # რგოლების რაოდენობა
r1 = R / np.sqrt(N_bins)  # რგოლის რადიუსის მაშტაბი
n_array = np.arange(N_bins + 1)  # რგოლების რაოდენობის მასივი [0, 1, 2, 3, 4, 5]
r_min = 0.5 * r1  # რგოლის მინიმალური რადიუსი
bins = r_min + (R - r_min) * np.sqrt(n_array / N_bins)  # ტოლფართობიანი რგოლების

t = np.linspace(0, 2 * np.pi, 500)  # კუთხეები წრეწირის ასაგებად

plt.figure()

plt.scatter(X, Y, color="lightgray", s=1)  # ყველა წერტილი რუხია

plt.scatter(X_sel, Y_sel, color="red", s=1)  # არჩეული წერტილები

for radius in bins:  # რგოლების რადიუსის ციკლი
    x_circle = x_c + radius * np.cos(t)  # რგოლის X - კოორდინატები
    y_circle = y_c + radius * np.sin(t)  # რგოლის Y - კოორდინატები
    plt.plot(x_circle, y_circle, color="black", alpha=0.3)  # რგოლის დახატვა

plt.scatter([x_c], [y_c], color="red", s=20)  # ცენტრის დახატვა

plt.title("Particles with radial bins")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()

counts, edges = np.histogram(r, bins=bins)  # ვითვლი რამდენი ვარსკვლავია თითოეულ რგოლში

r_mid = 0.5 * (edges[:-1] + edges[1:])  # რგოლების შუები

# რადიუსების მიხედვით განაწილების გრაფიკი
plt.figure()
plt.plot(r_mid, counts, linewidth=2)


plt.title("Radial density (equal-area rings)")
plt.xlabel("r")
plt.ylabel("number of particles")
plt.grid()
plt.show()


dx = X_sel - x_c  # ყველა ვარსკვლავის X - ღერძიდან დაშორება
dy = Y_sel - y_c  # ყველა ვარსკვლავის Y - ღერძიდან დაშორება

vx_c = np.mean(
    v_1[mask]
)  # X - ღეძის მიმართ არჩეულ მიდამოში ვარსკვლავენბის საშუალო სიჩქარე
vy_c = np.mean(
    v_2[mask]
)  # Y - ღეძის მიმართ არჩეულ მიდამოში ვარსკვლავენბის საშუალო სიჩქარე
vx_rel = (
    v_1[mask] - vx_c
)  # X - ღეძის მიმართ არჩეულ მიდამოში ვარსკვლავენბის სიჩქარე ცენტრის მიმართ
vy_rel = (
    v_2[mask] - vy_c
)  # Y - ღეძის მიმართ არჩეულ მიდამოში ვარსკვლავენბის სიჩქარე ცენტრის მიმართ


L_z = (
    dx * vy_rel - dy * vx_rel
)  # L_z = (x - x_c) * vx_rel - (y - y_c) * vy_rel (კუთხური მომენტის z - კომპონნენტა)

print("Mean L_z:", np.mean(L_z))  # ყველა ვარსკვლავის საშუალო კუთხური მომენტი
print(
    "Median L_z:", np.median(L_z)
)  # მედიანური კუთხური მომენტი (სორტირების შემდეგ ცენტრალური მნიშვნელობა)
print(
    "Negative fraction =", np.mean(L_z < 0)
)  # ვარსკვლავები უარყოფითი კუთხური მომენტით (შეესაბამება საათის ისრით მიმართულებით მოძრაობას)
print(
    "Positive fraction =", np.mean(L_z > 0)
)  # ვარსკვლავები დადებითი კუთხური მომენტით (შეესაბამება საათის ისრის საწინააღმდეგო მიმართულებით მოძრაობას)

plt.figure()
plt.hist(L_z, bins=50)  # კუთხური მომენტების განაწილების ჰისტოგრამა
plt.title("L_z distribution")  # სათაური
plt.xlabel("L_z")  # X - ღერძი
plt.ylabel("Number of stars")  # Y - ვარსკვლავების რაოდენობა
plt.title("Angular momentum distribution")
plt.show()
