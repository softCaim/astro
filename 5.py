def Amoxsnebi():
    Okulardict = []

    while True:

        try:
            Gamadidebloba = float(input("Enter enlarger: "))

            if Gamadidebloba == 0:
                break

            Fokal = float(input("Enter focal distance: "))
            Okular = Fokal/Gamadidebloba

            Okulardict.append({f"Okular distance from fokal point - {Okular}"})

        except ValueError:
           print("Please enter a valid number")

        print(Okulardict)


Amoxsnebi()
