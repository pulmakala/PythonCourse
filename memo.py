# Tehtävänä oli rakentaa muistikirja, joka käyttää merkintöjen hallintaan Pythonin lista-tietorakennetta
# ja tallentaa muistikirjan bittimuotoisena tietokoneen levylle. Ohjelmassa piti olla seuraavat ominaisuudet:
# A) Ohjelmaan voidaan lisätä merkintöjä, joissa on samanlainen aikaleima kuin aiemmin.
# B)Ohjelmassa voi valita merkinnän listalta, ja korvata sen uudella.
# C)Ohjelmalla voi poistaa yksittäisen merkinnän listalta, sekä
# D)Ohjelma lataa aiemmin luodun listan ohjelman käynnistyessä mikäli sellainen on olemassa.
#
# Ohjelma käyttää tietokantanaan tiedostoa nimeltä "muistio.dat". Käynnistyessään ohjelma koittaa ladata aiemmin
# luodun listan ko. tiedostosta, tai mikäli tällaista ei ole olemassa tai sen lataaminen tuottaa virheen, luo uuden
# ilmoittaen "Virhe tiedostossa, luodaan uusi muistio.dat.". Tämän jälkeen käyttäjä voi lisätä merkintöjä listalle.

# -*- coding: cp1252 -*-

import time
import pickle

#luodaan oletusmuistio sekä lista
tiedostonNimi = "muistio.dat"
lista = []

try:
    tiedosto = open(tiedostonNimi, "rb")
    lista = pickle.load(tiedosto)
    tiedosto.close()
except IOError:
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    tiedosto = open(tiedostonNimi, "wb")

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta\n")
    valinta = int(input("Mitä haluat tehdä?: "))

    if valinta == 1:
        for i in lista:
            print(i)
    elif valinta == 2:
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        uusi = lisays + ":::" + aika
        lista.append(uusi)
        pickle.dump(lista, tiedosto)
    elif valinta == 3:
        try:
            pituus = len(lista)
            print("Listalla on", pituus, "merkintää.")
            muutetaan = int(input("Mitä niistä muutetaan?: "))
            muutetaan = muutetaan - 1
            print(lista[muutetaan])
        except IndexError:
            print("Virheellinen valinta.")
        else:
            muokataan = input("Anna uusi teksti: ")
            aika = time.strftime("%X %x")
            uusiMuokkaus = muokataan + ":::" + aika
            lista.pop(muutetaan)
            lista.insert(muutetaan, uusiMuokkaus)
            tiedosto = open(tiedostonNimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
    elif valinta == 4:
        pituus = len(lista)
        print("Listalla on", pituus, "merkintää.")
        poistetaan = int(input("Mitä niistä poistetaan?: "))
        try:
            poistetaan = poistetaan - 1
            print("Poistettiin merkintä", lista[poistetaan])
            lista.pop(poistetaan)
            tiedosto = open(tiedostonNimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
        except IndexError:
            print("Virheellinen valinta.")
    elif valinta == 5:
        tiedosto = open(tiedostonNimi, "wb")
        pickle.dump(lista, tiedosto)
        tiedosto.close()
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")