"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Milan Novák
email: novakmilan@email.cz
discord: milannovak_77018
"""
from random import randrange 
import time

# promenne pro statistiku her
statistika = []
hry = 1

while True:
    # promenne pro hru
    cislo_uzivatel = ""
    pokusy = 0
    list_nahodne_start = []
    list_nahodne = []
    list_uzivatel = []

    # uvodni text
    cara = "-" * 47
    print("Hi there!")
    print(cara)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(cara)

    # zacatek mereni casu
    cas_zacatek = time.time()
    
    # generovani nahodneho 4-mistneho cisla jako list; prvni neni 0, není duplicita
    list_nahodne_start.append(str(randrange(1,10)))
    while len(list_nahodne_start) != 4:
        prvek_nahodne = str(randrange(0,10))
        if prvek_nahodne not in list_nahodne_start:
            list_nahodne_start.append(prvek_nahodne)
    print(list_nahodne_start)
        
    # nekonecna smycka
    while True:
        # vstup uzivatele, kontrola vstupu; má 4 znaky, obsahuje jen čísla, nezačíná nulou, není duplicita
        cislo_uzivatel = input("Enter a number: ")
        while True:
            if len(cislo_uzivatel) != 4 or not cislo_uzivatel.isdigit() or         cislo_uzivatel[0] == "0":
                cislo_uzivatel = input("Wrong input! Try again.\nEnter a number: ")
                continue
            if len(set(cislo_uzivatel)) != 4:
                cislo_uzivatel = input("Wrong input! Try again.\nEnter a number: ")
                continue
            break 

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
            if byci == 1:
                byk = "bull"
            else:
                byk = "bulls"
            if kravy == 1:
                krava = "cow"
            else:
                krava = "cows"
            print(byci, byk, kravy, krava)
            print(cara)
        else:
            # uhodnuto
            # konec mereni casu, tisk
            cas_konec = time.time()
            cas_celkem = round(cas_konec - cas_zacatek, 1)
            print("Correct, you've guessed the right number \nin", pokusy, "guesses!\nYour time:", cas_celkem, "seconds.\n")
            
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
    # statistika
    print()
    print(cara)
    print("Your statistics")
    print(cara)
    statistika.append(hry)
    statistika.append(pokusy)
    statistika.append(cas_celkem)
        
    for i in range(0, len(statistika), 3):
        print("Game #", statistika[i], "  Guesses: ", statistika[i + 1], "\nYour time: ", statistika[i+2], " sec\n", sep = "")
    print(cara)
    if input("Wanna play again? (y/n) ") == "y":
        hry += 1
        print()
        print(cara)
        continue
    else:
        print("Thanks for playing! Bye.")
        break