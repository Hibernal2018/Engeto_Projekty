# projekt 2
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Milan Novák
email: novakmilan@email.cz
discord: milannovak_77018
"""
from random import randrange 

# zavedeni promennych
cislo_uzivatel = ""
pokusy = 0
list_nahodne_start = list()
list_nahodne = list()
list_uzivatel = list()

# uvodni text
cara = "-" * 47
print("Hi there!")
print(cara)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(cara)

# generovani nahodneho 4-mistneho cisla jako list
[list_nahodne_start.append(str(randrange(0,10))) for i in range(4)]    

# nekonecny cyklus
while True:
    # vstup uzivatele, kontrola vstupu
    cislo_uzivatel = input("Enter a number: ")
    while len(cislo_uzivatel) != 4 or cislo_uzivatel.isalpha():
        cislo_uzivatel = input("Wrong input! Try again.\nEnter a number: ")

    # prevod cisla uzivatele na list
    [list_uzivatel.append(cislo_uzivatel[i]) for i in range(4)]
    print(cara)

    # pocitadlo pokusu
    pokusy += 1

    # je uhodnuto? nulovani promennych byci, kravy, kopirovani puvodnich odnot do listu nahodne 
    if list_uzivatel != list_nahodne_start:
        byci = 0
        kravy = 0
        list_nahodne = list_nahodne_start.copy()

        # cyklus prochazi oba listy; vyskyt a zaroven shoda na danem indexu = bulls , vyskyt v listu nahodne = cows
        # zaroven prvky na danem indexu vymaze a nahradi znaky x, y, resp. a
        for i in range(4):
            if list_uzivatel[i] == list_nahodne[i]:
                byci += 1
                list_uzivatel.pop(i)
                list_uzivatel.insert(i, "x")
                list_nahodne.pop(i)
                list_nahodne.insert(i, "y")
        for j in range(4):
            if list_uzivatel[j] in list_nahodne:
                kravy += 1
                index_kravy = list_nahodne.index(list_uzivatel[j])
                list_nahodne.pop(index_kravy)
                list_nahodne.insert(index_kravy, "a")
        list_uzivatel.clear()

        # tisk, rozliseni jednoneho a mnozneho cisla
        if byci == 1 and kravy != 1:
            print(byci, "bull", kravy, "cows")
        elif byci != 1 and kravy == 1:
            print(byci, "bulls", kravy, "cow")
        else:
            print(byci, "bulls", kravy, "cows")
        print(cara)
    else:
        print("Correct, you've guessed the right number \nin", pokusy, "guesses!")
        print(cara)

        # vyhodnoceni podle poctu pokusu
        if pokusy  < 5:
            print("That´s amazing!")
        elif pokusy  < 10:
            print("That´s good.")
        elif pokusy  < 15:
            print("That´s not so good.")
        else:
            print("Disaster bro...!")
        break