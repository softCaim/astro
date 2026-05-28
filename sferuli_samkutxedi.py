import json
import math


def sin(x):
    if x is not None:
        return math.sin(math.radians(x))
    return None


def arcsin(x):
    if x is not None:
        angle = math.degrees(math.asin(x))
        angle_2 = 180 - angle
        return angle, angle_2
    return None


def cos(x):
    if x is not None:
        return math.cos(math.radians(x))
    return None


def arcos(x):
    if x is not None:
        angle = math.degrees(math.acos(x))
        return angle
    return None


with open("spher.json") as f:
    data = json.load(f)

for i in data:
    a = i.get("a")
    b = i.get("b")
    c = i.get("c")
    C = i.get("C")
    B = i.get("B")
    A = i.get("A")

    missing = {
        "a": "a" in i and i["a"] is None,
        "b": "b" in i and i["b"] is None,
        "c": "c" in i and i["c"] is None,
        "A": "A" in i and i["A"] is None,
        "B": "B" in i and i["B"] is None,
        "C": "C" in i and i["C"] is None,
    }

    if a is not None and b is not None and c is not None and missing["C"]:
        mricxveli = cos(c) - cos(a) * cos(b)
        mnishvneli = sin(a) * sin(b)
        C = arcos(mricxveli / mnishvneli)
        i["C"] = C

    elif a is not None and b is not None and C is not None and missing["c"]:
        c = arcos(cos(a) * cos(b) + sin(a) * sin(b) * cos(C))
        i["c"] = c

    elif a is not None and C is not None and b is not None and missing["B"]:
        mricxveli = sin(C) * sin(b)
        c = arcos((cos(a) * cos(b)) + (sin(a) * sin(b) * cos(C)))
        mnishvneli = sin(c)
        B, B_1 = arcsin(mricxveli / mnishvneli)

        if b > a and b > c:
            if B > B_1:
                i["B"] = B
            else:
                i["B"] = B_1
        else:
            i["B"] = B
            i["B_1"] = B_1

    elif a is not None and b is not None and A is not None and missing["c"]:
        B, B_1 = arcsin(sin(b) * sin(A) / sin(a))
        mricxveli = (cos(a) * cos(b)) - (sin(a) * sin(b) * cos(A) * cos(B))
        mnishvneli = 1 - (sin(A) * sin(B) * sin(a) * sin(b))
        c = arcos(mricxveli / mnishvneli)
        mricxveli = (cos(a) * cos(b)) - (sin(a) * sin(b) * cos(A) * cos(B_1))
        mnishvneli = 1 - (sin(A) * sin(B_1) * sin(a) * sin(b))
        c_1 = arcos(mricxveli / mnishvneli)
        i["c"] = c
        i["c_1"] = c_1

    elif a is not None and b is not None and A is not None and missing["B"]:
        mricxveli = sin(A) * sin(b)
        mnishvneli = sin(a)
        B, B_1 = arcsin(mricxveli / mnishvneli)
        if (sin(a) / sin(A)) == (sin(b) / sin(B)) == (sin(b) / sin(B_1)):
            i["B"] = B
            i["B_1"] = B_1
        else:
            if (sin(a) / sin(A)) == (sin(b) / sin(B)):
                i["B_1"] = B
            elif (sin(a) / sin(A)) == (sin(b) / sin(B_1)):
                i["B_1"] = B_1
            else:
                i["B"] = None
                i["B_1"] = None

    elif a is not None and b is not None and A is not None and missing["C"]:
        B, B_1 = arcsin(sin(b) * sin(A) / sin(a))
        mricxveli = (sin(A) * sin(B) * cos(a) * cos(b)) - cos(A) * cos(B)
        mnishvneli = 1 - (sin(A) * sin(B) * sin(a) * sin(b))
        C = arcos(mricxveli / mnishvneli)
        mricxveli_1 = (sin(A) * sin(B_1) * cos(a) * cos(b)) - cos(A) * cos(B_1)
        mnishvneli_1 = 1 - (sin(A) * sin(B_1) * sin(a) * sin(b))
        C_1 = arcos(mricxveli_1 / mnishvneli_1)
        i["C"] = C
        i["C_1"] = C_1

    elif c is not None and A is not None and B is not None and missing["a"]:
        C = arcos((sin(A) * sin(B) * cos(c)) - cos(A) * cos(B))
        a = arcos((cos(A) + (cos(B) * cos(C))) / (sin(B) * sin(C)))
        i["a"] = a

    elif c is not None and A is not None and B is not None and missing["C"]:
        C = arcos((sin(A) * sin(B) * cos(c)) - cos(A) * cos(B))
        i["C"] = C

    elif A is not None and B is not None and a is not None and missing["b"]:
        b, b_1 = arcsin(sin(a) * sin(B) / sin(A))
        i["b"] = b
        i["b_1"] = b_1

    elif A is not None and B is not None and a is not None and missing["c"]:
        b, b_1 = arcsin(sin(a) * sin(B) / sin(A))

        mricxveli = (cos(a) * cos(b) * sin(A) * sin(B)) - (cos(A) * cos(B))
        mnishvneli = 1 - (sin(b) * sin(a) * sin(B) * sin(A))
        c = arcos((cos(a) * cos(b)) + (sin(a) * sin(b) * mricxveli / mnishvneli))

        mricxveli_1 = (cos(a) * cos(b_1) * sin(A) * sin(B)) - (cos(A) * cos(B))
        mnishvneli_1 = 1 - (sin(b_1) * sin(a) * sin(B) * sin(A))
        c_1 = arcos(
            (cos(a) * cos(b_1)) + (sin(a) * sin(b_1) * mricxveli_1 / mnishvneli_1)
        )

        i["c"] = c
        i["c_1"] = c_1

    elif A is not None and B is not None and a is not None and missing["C"]:
        b, b_1 = arcsin(sin(a) * sin(B) / sin(A))

        pirveli = (cos(a) * cos(b)) - (sin(a) * sin(b) * cos(A) * cos(B))
        meore = 1 - (sin(b) * sin(a) * sin(B) * sin(A))
        mricxveli = (pirveli / meore) - (cos(a) * cos(b))
        mnishvneli = sin(a) * sin(b)
        C = arcos(mricxveli / mnishvneli)

        pirveli_1 = (cos(a) * cos(b_1)) - (sin(a) * sin(b_1) * cos(A) * cos(B))
        meore_1 = 1 - (sin(b_1) * sin(a) * sin(B) * sin(A))
        mricxveli_1 = (pirveli_1 / meore_1) - (cos(a) * cos(b_1))
        mnishvneli_1 = sin(a) * sin(b_1)
        C_1 = arcos(mricxveli_1 / mnishvneli_1)

        i["C"] = C
        i["C_1"] = C_1

    elif A is not None and B is not None and C is not None and missing["c"]:
        mricxveli = cos(C) + (cos(A) * cos(B))
        mnishvneli = sin(A) * sin(B)
        c = arcos(mricxveli / mnishvneli)
        i["c"] = c


with open("spher_tr.json", "w") as f:
    json.dump(data, f, indent=4)
