import math

def replaceier(x):
    if "h" in x:
        parts = x.replace("h", " ").replace("m", " ").replace("s", " ").split()

    elif "°" in x:
        parts = x.replace("°", " ").replace("'", " ").replace("\"", " ").split()

    return parts

def ateulebi(x):
    c = replaceier(x)

    first = int(c[0])
    second = int(c[1])
    third = int(c[2])

    return round(first + second/60 + third/3600, 6)

def hour_to_grad(x):

    return x * 15

'''ტრიგონომეტრიული ფუნქციები'''

def sin(x):
    
    return math.sin(math.radians(x))


def cos(x):

    return math.cos(math.radians(x))


def arccos(x):

    return math.degrees(math.acos(x))

def arcsin(x):
    
    angle = math.degrees(math.asin(x))

    return angle

'''--------------------------------'''


H = "5h51m44s"
delta = ' 23°13\'10" '


dec = ateulebi(H)

phi = 52

sina = round(sin(ateulebi(delta))*sin(phi) + cos(ateulebi(delta))*cos(phi)*cos(hour_to_grad(dec)), 6)

a = round(arcsin(sina), 6)

mricxveli = sin(ateulebi(delta)) - sin(phi)*sin(a)

mnishvneli = cos(phi)*cos(a)

cosA = round(mricxveli/mnishvneli, 6)

A_1 = round(arccos(cosA), 6)

sinH = round(sin(hour_to_grad(dec)), 6)

def azimut(x, A_1):
    if x > 0:
        A = 360 - A_1


    else:
        A = A_1

    return A

Adm = azimut(sinH, A_1)




def gradusa(x):
    grad = int(x)
    minute = (x%1) * 60
    min_mod = int(minute)
    sec = round((minute - min_mod)*60, 2)

    return grad, min_mod, sec

def sheerteba(x):
    d, m, s = gradusa(x)

    return f"{d}°{m}'{s}\" "


print(f"{dec}H")
print(f"{hour_to_grad(dec)}°")
print(f"{ateulebi(delta)}°")
print(sina)
print(a)
print(cosA)
print(f"A' = {A_1}°")
print(sinH)
print(Adm)
print(sheerteba(a))
print(sheerteba(Adm))


