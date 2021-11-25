# Tehtävänä oli tehdä ohjelma, jossa luodaan kaksi oliota ja annetaan näille alustuksessa värit,
# jonka jälkeen kutsutaan molempien tilanne-jäsenfunktiota. Lopuksi tulostetaan ensimmäisen olion selosteteksti.
# Tehtävässä tuli hyödyntää alustusfunktiota __init__ ja jäsenfunktiota.

# -*- coding: cp1252 -*-

class Kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""
    vari = ""
    pisteet = ""

    def __init__(self):
        self.vari = input("Anna minulle väri: ")

    def tilanne(self):
        print("Olen", self.vari, "ja minulla on", self.pisteet, "pistettä!")

    def maali(self):
        self.pisteet = + 1

def main():
    eka = Kilpailija()
    toka = Kilpailija()
    eka.pisteet = 0
    toka.pisteet = 0
    eka.tilanne()
    toka.tilanne()
    print(eka.__doc__)


if __name__ == "__main__":
    main()