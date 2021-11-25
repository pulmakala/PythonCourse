# Tehtävänä on tarkistaa merkkijonoja.txt-nimisestä tiedostosta, mitkä merkkijonot kelpaavat salasanaksi,
# eli onko merkkijono sellainen, joka sisältää vain kirjaimia ja numeroita.

# -*- coding: cp1252 -*-

tiedosto = open("merkkijonoja.txt", "r")

for salasana in tiedosto:
	if salasana.strip("\n").isalnum():
		print(salasana[:-1],"kelpaa salasanaksi.")
	else:
		print(salasana[:-1],"sisältää virheellisiä merkkejä.")

tiedosto.close()