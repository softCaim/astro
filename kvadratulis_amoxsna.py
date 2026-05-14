a = complex(input("Enter a complex number: "))
b = complex(input("Enter another complex number: "))
c = complex(input("Enter another complex number: "))

def kvadratuli(a, b, c):
    Discriminant = b**2 - 4*a*c

    if Discriminant == 0:
        x = -b / (2*a)
        print(f"x = {x:.2f}")
    else:
        x_1 = (-b + Discriminant**0.5) / (2*a)
        x_2 = (-b - Discriminant**0.5) / (2*a)
        print(f"x_1 = {x_1:.2f}, x_2 = {x_2:.2f}")


result = kvadratuli(a, b, c)
