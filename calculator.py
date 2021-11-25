# Tehtävänä oli tehdä nelilaskin. Käyttäjän antamat syötteet tarkastetaan ennen kuin ne hyväksytään
# laskimeen numeroiksi. Suositus oli tehdä tämä luomalla erillinen alifunktio, joka pyytää
# käyttäjältä niin kauan uutta lukua kunnes tyyppimuunnos kokonaisluvuksi onnistuu. Tämän jälkeen
# alifunktio palauttaa lukuarvon laskimelle. Jos käyttäjän syöttämä luku on virheellinen,
# tulostetaan "Virheellinen syöte!" ja lukua pyydetään uudestaan.

# -*- coding: cp1252 -*-

# importit kuntoon
import math

# kysytään ja tarkistetaan luvut
def tarkistaLuvut():
    while True:
        try:
            luku = int(input("Anna luku: "))
            break
        except ValueError:
            print("Virheellinen syöte!")
            continue
    return luku

def main():
    # kysytään käyttäjältä lukuja
    luku1 = tarkistaLuvut()
    luku2 = tarkistaLuvut()
    jatkuu = True

    while jatkuu:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")

        print("Valitut luvut:", luku1, luku2)
        valinta = int(input("Tee valinta (1-8): "))

        if valinta == 1:
            tulos = luku1 + luku2
            print("Tulos on:", tulos)
        elif valinta == 2:
            tulos = luku1 - luku2
            print("Tulos on:", tulos)
        elif valinta == 3:
            tulos = luku1 * luku2
            print("Tulos on:", tulos)
        elif valinta == 4:
            tulos = float(luku1) / float(luku2)
            #tai tulos = luku1 / luku2
            tulos = float(tulos)
            print("Tulos on:", tulos)
        elif valinta == 5:
            tulos = math.sin(luku1 / luku2)
            print("Tulos on:", tulos)
        elif valinta == 6:
            tulos = math.cos(luku1 / luku2)
            print("Tulos on:", tulos)
        elif valinta == 7:
            luku1 = tarkistaLuvut()
            luku2 = tarkistaLuvut()
        elif valinta == 8:
            break
        else:
            print("Valintaa ei tunnistettu.")

if __name__ == "__main__":
	main()