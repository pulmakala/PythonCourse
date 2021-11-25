# Tehtävässä tutustuttiin random-moduulikirjaston toimintaan. Tehtävänä oli luoda ohjelma, joka arpoo 5 kertaa
# joko luvun 0 tai 1. Mikäli ohjelma arpoo luvun 1, tulostetaan "Kruuna!", ja mikäli 0, tulostetaan "Klaava!".

# -*- coding: cp1252 -*-

from random import randint

def lukupeli():
    kierros = 1

    print("Heitetään kolikkoa viidesti:")

    while kierros <= 5:
        luku = randint(0, 100)
        if luku == 1:
            print("Kruuna!")
        else:
            print("Klaava!")
        kierros = kierros + 1

if __name__ == "__main__":
    lukupeli()