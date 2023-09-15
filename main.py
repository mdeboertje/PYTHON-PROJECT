def bereken_bmi(gewicht, lengte):
    bmi = gewicht / (lengte * lengte)

    return bmi


def bereken_bmr(geslacht, gewicht, lengte, leeftijd):
    if geslacht == "man":
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * lengte) - (5.677 * leeftijd)

        return bmr
    elif geslacht == "vrouw":
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * lengte) - (4.330 * leeftijd)

        return bmr
    raise ValueError("Ongeldig geslacht. probeer opnieuw")


def bereken_energieverbuik(duur, intensiteitspercentage):
    epoc = 0.2 * duur * intensiteitspercentage
    energieverbruik = 7 * epoc
    return energieverbruik


def bereken_hartslagzone(leeftijd, rusthartslag, intensiteitspercentage):
    max_hartslag = 220 - leeftijd
    reserve_hartslag = max_hartslag - rusthartslag
    lower_limit = rusthartslag + (reserve_hartslag * intensiteitspercentage)
    upper_limit = rusthartslag + (reserve_hartslag * intensiteitspercentage) * 1.2
    hartslagzone = (lower_limit, upper_limit)

    return hartslagzone

def print_hoofdmenu():
    choice = int(input(
        "Hallo! maak een keuze uit:"
        "\n1. Bmi berekenen "
        "\n2. BMR berekenen "
        "\n3. Energising berekenen "
        "\n4. Hartslagzone berekenen"))

    while True:
        match choice:
            case 1:
                print("Voor het berekenen van uw BMI, hebben wij uw gewicht en lengte nodig")
                gewicht = float(input("Gewicht"))
                lengte = float(input("Lengte"))
                bmi = bereken_bmi(gewicht, lengte)
                print(f"Uw bmi is: {bmi: 2f}")
            case 2:
                print("Voor het berekenen van uw BMR, hebben wij uw geslacht, gewicht, lengte en leeftijd nodig.")
                geslacht = input("Geslacht: Man of Vrouw")
                gewicht = float(input("Gewicht"))
                lengte = float(input("Lengte"))
                leeftijd = int(input("Leeftijd"))
                bmr = bereken_bmr(geslacht.lower(), gewicht, lengte, leeftijd)
                print(f"Uw BMR is: {bmr: 2f}")
            case 3:
                print("Voor het berekenen van uw energie/caloriën verbruik "
                      "hebben wij de duur en het intensiteits "
                      "percentage nodig")
                duur = float(input("Duur van de training"))
                intensiteit = int(input("Intensiteit van training"))
                energieverbruik = bereken_energieverbuik(duur, intensiteit)
                print(energieverbruik)
            case 4:
                print("Voor het berekenen van uw hartslagzonek"
                      "hebben wij uw leeftijd, rusthartslag en intensiteitspercentage nodig")
                leeftijd = int(input("Voer je leeftijd in: "))
                rusthartslag = int(input("Voer je rusthartslag in: "))
                intensiteitspercentage = float(input("Voer het intensiteitspercentage in (0-1): "))
                hartslagzone = bereken_hartslagzone(leeftijd, rusthartslag, intensiteitspercentage)
                print(f"Je hartslagzone is: {hartslagzone[0]} - {hartslagzone[1]} slagen per minuut")


def main():
    print_hoofdmenu()


if __name__ == '__main__':
    main()
