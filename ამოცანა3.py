def law():
    Planets = []

    while True:
        Planet_name = input("Enter planet name: ").strip()

        if Planet_name == "stop" or Planet_name == "":
            break

        Period = float(input("Enter period: "))
        Radius = float(input("Enter radius: "))

        Kepler_law = (Period**2)/Radius**3

        Planets.append({f"Kepler_law for {Planet_name} - {Kepler_law}"})

        print(Planets)

law()
