def reverse_kepler_law():

    period = 8.0
    radiuscube = (period**2)/1
    radius = round(radiuscube**(1/3))
    return radius

print(reverse_kepler_law())
