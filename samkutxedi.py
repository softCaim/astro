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
    a_c = i.get("a/c")
    b_c = i.get("b/c")

    missing = {
        "a": "a" in i and i["a"] is None,
        "b": "b" in i and i["b"] is None,
        "c": "c" in i and i["c"] is None,
        "A": "A" in i and i["A"] is None,
        "B": "B" in i and i["B"] is None,
        "C": "C" in i and i["C"] is None,
        "a/c": "a/c" in i and i["a/c"] is None,
        "b/c": "b/c" in i and i["b/c"] is None,
    }

    if a and b and c:
        if a + b <= c or a + c <= b or b + c <= a:
            i["error"] = "Not a triangle"
            continue

    if a is not None and b is not None and c is not None and missing["C"]:
        Cos_c = (a**2 + b**2 - c**2) / (2 * a * b)
        if Cos_c > 1 or Cos_c < -1:
            i["error"] = "Not a triangle"
            continue
        else:
            C = math.degrees(math.acos(Cos_c))
            i["C"] = C

    elif a is not None and b is not None and C is not None and missing["c"]:
        c = math.sqrt(a**2 + b**2 - 2 * b * a * math.cos(math.radians(C)))
        i["c"] = c

    elif a is not None and b is not None and C is not None and missing["B"]:
        c = math.sqrt(a**2 + b**2 - 2 * b * a * math.cos(math.radians(C)))
        Sin_B = math.sin(math.radians(C)) * b / c
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue
        else:
            B = math.degrees(math.asin(Sin_B))
            B_1 = 180 - B
            i["B"] = B
            if B_1 + C > 180:
                i["B_1"] = "Not valid"
                continue
            else:
                i["B_1"] = B_1

    elif a is not None and b is not None and A is not None and missing["c"]:
        Sin_B = (b * math.sin(math.radians(A))) / a
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue

        B = math.degrees(math.asin(Sin_B))
        C = 180 - A - B

        if C > 0:
            c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))
            i["c"] = c

        B_1 = 180 - B
        C_1 = 180 - A - B_1

        if C_1 > 0:
            c_1 = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C_1)))
            i["c_1"] = c_1

    elif a is not None and b is not None and A is not None and missing["B"]:
        Sin_B = (b * math.sin(math.radians(A))) / a
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue
        B = math.degrees(math.asin(Sin_B))
        i["B"] = B
        if B + A >= 180:
            i["error"] = "Not a triangle"
            continue
        else:
            B_1 = 180 - B
            if B_1 + A >= 180:
                i["B_1"] = "Not valid"
                continue
            else:
                i["B_1"] = B_1

    elif a is not None and b is not None and A is not None and missing["C"]:
        Sin_B = (b * math.sin(math.radians(A))) / a
        if Sin_B > 1 or Sin_B < -1:
            i["error"] = "Not a triangle"
            continue
        B = math.degrees(math.asin(Sin_B))
        if B + A >= 180:
            i["error"] = "Not a triangle"
            continue
        else:
            C = 180 - A - B
            i["C"] = C
            B_1 = 180 - B
            if B_1 + A >= 180:
                i["B_1"] = "Not valid"
                continue
            else:
                C_1 = 180 - B_1 - A
                i["C_1"] = C_1

    elif A is not None and B is not None and missing["a/c"] and missing["b/c"]:
        C = 180 - A - B

        x = math.sin(math.radians(A)) / math.sin(math.radians(C))
        y = math.sin(math.radians(B)) / math.sin(math.radians(C))

        i["a/c"] = x
        i["b/c"] = y
        print(x, y)

with open("new.json", "w") as w:
    json.dump(data, w, indent=4)
