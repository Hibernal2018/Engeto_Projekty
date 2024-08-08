"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Milan Novák
email: novakmilan@email.cz
discord: milannovak_77018
"""
# zavedeni promennych
vitezne_pozice = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]
]
pole = ["|   "] * 10
pozice_x = []
pozice_o = []
oddelovac = "=" * 50
vstup_x = ""

# funkce pro zobrazeni hraciho pole
def tiskni_obrazec(seznam : list) -> list:
    print("+---+---+---+")
    for i in range(1, len(seznam)):
        if i % 3 == 0:
            print(seznam[i], end = "")
            print("|\n", end = "")
            print("+---+---+---+")
        else:
            print(seznam[i], end = "")
    print()

# funkce pro dolneni listu pole a pozice o volbu hrace
def dopln_volbu_hrace(seznam, seznam_hrac, vstup, znak):
    seznam_hrac.append(vstup)
    seznam.pop(vstup)
    pole.insert(vstup, f"| {znak} ")

# funkce pro kontrolu vyhry
def zkontroluj_vyhru(vitezne, pozice_1, znak):
    for listy_vyher in vitezne:
        pocitadlo = 0
        for prvky in listy_vyher:
           if prvky in pozice_1:
               pocitadlo += 1
        if pocitadlo == 3:
            print(f"{oddelovac}\nCongratulations, the player {znak} WON!\n{oddelovac}")
            return True
    return False

# funkce pro kontrolu remizy
def zkontroluj_remizu(pozice_1, pozice_2): 
    if len(pozice_1) + len(pozice_2) == 9:
        print(f"{oddelovac}\nIt´s a tie...\n{oddelovac}")
        return True
    return False

# uvodni text
print("""
    Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
    """)
        
# vlastni hra
while True:
    # uvodni obrazec
    tiskni_obrazec(pole)
    konec = False
    while True:
        # vstup a kontrola vstupu a duplicity
        while True:
            print(oddelovac)
            vstup_o = (input("Player o | Please enter your move number (1-9): "))
            print(oddelovac)
            if not vstup_o.isnumeric():
                print("Player o | Your choice is not a number! Try again.")
                continue
            vstup_o = int(vstup_o)
            if vstup_o not in range(1, 10):
                print("Player o | Your choice is out of range!. Try again.")
            if vstup_o not in pozice_x and vstup_o not in pozice_o:
                dopln_volbu_hrace(pole, pozice_o, vstup_o, "O")
                tiskni_obrazec(pole)
                break
            else:
                print("This position is already taken. Try another one.\n")
                continue
        if zkontroluj_vyhru(vitezne_pozice, pozice_o, "O"):
            konec = True
            break
        if zkontroluj_remizu(pozice_o, pozice_x):
            konec = True
            break
        while True:
            # vstup a kontrola vstupu a duplicity
            print(oddelovac)
            vstup_x = (input("Player x | Please enter your move number (1-9): "))
            print(oddelovac)
            if not vstup_x.isnumeric():
                print("Player x | Your choice is not a number! Try again.")
                continue
            vstup_x = int(vstup_x)
            if vstup_x not in range(1, 10):
                print("Player x | Your choice is out of range! Try again.")
                continue
            if vstup_x not in pozice_x and vstup_x not in pozice_o:
                dopln_volbu_hrace(pole, pozice_x, vstup_x, "X")
                tiskni_obrazec(pole)
                break
            else:
                print("This position is already taken. Try another one.\n")
                continue
        if zkontroluj_vyhru(vitezne_pozice, pozice_x, "X"):
            konec = True
            break
        if zkontroluj_remizu(pozice_o, pozice_x):
            konec = True
            break
    if konec:
        if input("Wanna play again? (y/n) ") == "y":
            pole = ["|   "] * 10
            pozice_x = []
            pozice_o = []
            continue
        else:
            break 