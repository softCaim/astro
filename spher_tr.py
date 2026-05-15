import json
import math
from turtle import degrees

with open("spher.json", "r") as f:
    data = json.load(f)


"""def find_variable(i):
    for key in ["a", "b", "c", "C", "A", "B"]:
        if i.get(key) is None:
            return key
    return None"""


def solver(i):
    a = i.get("a")
    b = i.get("b")
    c = i.get("c")
    C = i.get("C")
    A = i.get("A")
    B = i.get("B")

    if C is None and a is not None and b is not None and c is not None:
        Cos_c = (
            math.cos(math.radians(c))
            - math.cos(math.radians(b)) * math.cos(math.radians(a))
        ) / (math.sin(math.radians(a)) * math.sin(math.radians(b)))
        C = math.degrees(math.acos(Cos_c))
        i["C"] = C

    if c is None and a is not None and b is not None and C is not None:
        Cos_c = math.cos(math.radians(a)) * math.cos(math.radians(b)) + math.sin(
            math.radians(a)
        ) * math.sin(math.radians(b)) * math.cos(math.radians(C))
        c = math.degrees(math.acos(Cos_c))
        i["c"] = c

    if B is None and a is not None and b is not None and C is not None:
        Cos_B = (
            math.cos(math.radians(b))
            - math.cos(math.radians(a)) * math.cos(math.radians(c))
        ) / (math.sin(math.radians(a)) * math.sin(math.radians(c)))
        acos = math.acos(Cos_B)
        B = math.degrees(acos)
        i["B"] = B

    # if a is not None and b is not None and A is not None and c is None


for t in data:
    solver(t)

with open("amosxnebi.txt", "w") as f:
    for l, item in enumerate(data):
        f.write(f"samkutxedi {l + 1}\n")
        for key, value in item.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")

print(math.cos(math.degrees(90)))
