import math


def kutxe():
    while True:
        try:
            r_sun = float(input("Enter the radius of the sun: ").strip())
            d_sun = float(input("Enter the distance from the sun: ").strip())
            radian = (2 * r_sun) / d_sun
            gradus = radian * (180 / math.pi)
            min = gradus * 60
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            continue

    while True:
        try:
            r_moon = float(input("Enter the radius of the moon: ").strip())
            d_moon = float(input("Enter the distance from the moon: ").strip())
            radian_moon = (2 * r_moon) / d_moon
            gradus_moon = radian_moon * (180 / math.pi)
            min_moon = gradus_moon * 60
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            continue

    print(
        f"მზესთან ხილული კუთხე: რადიანებში - {radian}, გრადუსებში ~ {gradus}, მინუტებში ~ {min} და მთავრესთან ხილული კუთხე: რადიანებში - {radian_moon}, გრადუსებში ~ {gradus_moon}, მინუტებში ~ {min_moon}"
    )


kutxe()
