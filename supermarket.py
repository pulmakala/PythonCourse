# Tehtävänantona oli tehdä yksinkertainen Supermarket-ohjelma, jossa kymmenen tuotteen hinnat ovat listassa.
# Ohjelmassa kysytään tuotteen numeroa väliltä 1-10, ja sitten ohjelma hakee listasta haettavan tuotteen hinnan,
# tulostaa tuotteen numeron sekä hinnan sekä laskee ostosten yhteissumman. 0 syöttäminen lopettaa silmukan, jolloin
# tulostetaan lopuksi tuotteiden kokonaissumma, pyydetään maksu, ja lasketaan vaihtorahat.

# -*- coding: cp1252 -*-

def supermarket():
    hinnat = [10,14,22,33,44,13,22,55,66,77]
    kokonaissumma = 0

    print("Supermarket\n===========")

    while True:
        valinta = int(input("Valitse tuote (1-10) 0 lopetus: "))
        if valinta > 0 and valinta < 11:
            haettava = hinnat[valinta-1]
            print("Tuote:\t", valinta, "Hinta:\t", haettava)
            kokonaissumma = kokonaissumma + haettava
        elif valinta == 0:
            print("Yhteensä: ", kokonaissumma)
            maksu = int(input("Maksu: "))
            print("vaihto: ", maksu-kokonaissumma)
            break
        else:
            print("Valintaa ei tunnistettu.")

def main():
    supermarket()
if __name__ == "__main__":
	main()