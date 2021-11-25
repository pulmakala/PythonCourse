# Tehtävänantona oli luoda luokka Employee, ja sille alustusmetodi. Ohjelmassa lisätään listaan
# Employee-olioita, id on laskennallinen järjestysnumero luvusta 1 alkaen ja nimi kysytään käyttäjältä.
# Lopussa tulostetaan listan sisältö.

# -*- coding: cp1252 -*-

class Employee:
    id = ""
    name = ""
    lauseke = ""

    employees = []
    def lisaa(self):
        self.lauseke = "Id: {0} Nimi: {1}".format(self.id, self.name)
        self.employees.append(self.lauseke)

    def tulosta(self):
        for i in range(0,len(self.employees)):
            print(self.employees[i])

def main():
    luku = 0

    while True:
        nimi = input("Anna työntekijän nimi: (0 lopetus):")
        if nimi == "0":
            Emp.tulosta()
            break
        else:
            Emp = Employee()
            Emp.id = luku + 1
            Emp.name = nimi
            Emp.lisaa()
            luku = luku + 1

if __name__ == "__main__":
    main()