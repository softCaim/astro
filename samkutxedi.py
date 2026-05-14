import json
import math

with open("triangle.json", "r") as f:
    data = json.load(f)


for i in data:
    a = i.get("a")
    b = i.get("b")
    c = i.get("c")
    C = i.get("C")
    B = i.get("B")
    A = i.get("A")

    if a and b and c:
        if a + b <= c or a + c <= b or b + c <= a:
            i["error"] = "Not a triangle"
            continue

    if a is not None and b is not None and c is not None and C is None:
        Cos_c = (a**2 + b**2 - c**2) / (2 * a * b)
        if Cos_c > 1 or Cos_c < -1:
            i["error"] = "Not a triangle"
            continue

        i["C"] = math.degrees(math.acos(Cos_c))
        changed = True

    elif a is not None and b is not None and C is not None and c is None:
        c = math.sqrt(a**2 + b**2 - 2 * b * a * math.cos(math.radians(C)))
        i["c"] = c

    elif a is not None and b is not None and C is not None and B is None:
        Sin_B = math.sin(math.radians(C)) * b / c
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue

        i["B"] = math.degrees(math.asin(Sin_B))

    elif a is not None and b is not None and A is not None and c is None:
        Sin_B = (b * math.sin(math.radians(A))) / a
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue

        B = math.degrees(math.asin(Sin_B))
        C = 180 - A - B
        i["B"] = B
        i["C"] = C

    elif a is not None and b is not None and A is not None and B is None:
        B = math.degrees(math.asin((a * math.sin(math.radians(A))) / b))
        i["B"] = B

    elif a is not None and b is not None and A is not None and C is None:
        C = 180 - A - B
        i["C"] = C

    elif A is not None and a is not None and b is not None and c is None:
        Sin_B = math.sin(math.radians(A)) * b / a
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue

        B = math.degrees(math.asin(Sin_B))
        C = 180 - A - B
        i["C"] = C

        x = math.sin(math.radians(A)) / math.sin(math.radians(C))
        y = math.sin(math.radians(B)) / math.sin(math.radians(C))

        i["a/c"] = x
        i["b/c"] = y

with open("new.json", "w") as w:
    json.dump(data, w, indent=4)
