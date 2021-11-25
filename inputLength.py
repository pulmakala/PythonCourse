# Tehtävänä on saada syötteenä parametri, jonka pituus mitataan, ja lisätä ohjelmaan paluuarvo.

# -*- coding: cp1252 -*-

def pituusmitta(sana):
    sana = len(sana)
    return sana

def main():
    jatkuu = True

    while jatkuu:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if sana == "Lopeta":
            jatkuu = False
        elif len(sana) == 0:
            print("Et antanut syötettä")
        else:
            sananpituus = pituusmitta(sana)
            print("Antamasi syöte oli", sananpituus, "merkkiä pitkä.")

if __name__ == "__main__":
    main()