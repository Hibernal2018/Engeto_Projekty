TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# prvni cast - overeni uzivatele
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Milan Novák
email: novakmilan@email.cz
discord: milannovak_77018
"""
print(" ")
print(" ")
# přihlášení oprávněného uživatele
cara = "-" * 40
user = dict(bob="123", ann="pass123", mike="password123", liz="pass123")  
# vstup uživ. jména a hesla a ověření shody
prihl_user = input("Zadejte, prosím, své uživatelské jméno: ")
prihl_password = input("Zadejte, prosím, své heslo: ")
# odpovídá přihl. jméno seznamu? odpovídá heslo přihl. jménu na stejné pozici?
if prihl_password == user.get(prihl_user):
    print("username:", prihl_user)
    print("paswword:", prihl_password)
    print(cara)
    print("Welcome to the app, ", prihl_user)
else:
    print()   
    print("$ python projekt1.py") 
    print("username:", prihl_user)
    print("paswword", prihl_password)
    print("unregistered user, terminating the program..")
    exit()    
 
# vyber textu
print("We have 3 texts to be analyzed.")
print(cara)
cislo_textu = int(input("Enter a number btw. 1 and 3 to select: "))
# je číslo 1 - 3?
while cislo_textu not in range(1, 4):
    cislo_textu = int(input("Enter a number btw. 1 and 3 to select: "))
print(cara)
text = TEXTS[cislo_textu - 1]  # zvoleny text jako index vychoziho textu

# vycisteni textu
text = text.replace("\n", " ")  # odstrani z textu prvni znak v zavorce a nahradi ho mezerou
text = text.replace(".", "")
text = text.replace(",", "")
text = text.split(" ")  # rozdeli string na list podle mezer
for i in range(0, text.count('')):  # odstrani z listtu prazdne prvky
    text.remove('')

# reseni zadani
pocet_slov = len(text)  # pocet prvku v listu = pocet slov v textu 
print("There are", pocet_slov, "words in the selected text.")

prvni_velke = 0  # prvky s velkym pocatecnim pismenem
for prvek_listu in text:  # cyklus prochází list text
    if prvek_listu.istitle():
        prvni_velke += 1
print("There are", prvni_velke, "titlecase words.")

vsechna_velka = 0  # prvky obsahujici jen velka pismena
for prvek_listu in text:  
    if prvek_listu.isupper() and prvek_listu.isalpha():
        vsechna_velka += 1
print("There are", vsechna_velka, "uppercase words.")

vsechna_mala = 0  # prvky obsahujici jen mala pismena
for prvek_listu in text:  
    if prvek_listu.islower():
        vsechna_mala += 1
print("There are", vsechna_mala, "lowercase words.")

cisla = 0  # prvky obsahujici jen cisla
for prvek_listu in text:  
    if prvek_listu.isnumeric():
        cisla += 1
print("There are", cisla, "numeric strings.")

soucet_cisel = 0  # soucet vsech cisel v listu
for prvek_listu in text:  
    if prvek_listu.isnumeric():
        soucet_cisel += int(prvek_listu)
print("The sum of all the numbers ", soucet_cisel)
print(cara)
print("LEN |    OCCURENCES    |NR.")
print(cara)

# pocet slov o delce x pismen
delka_prvku = []
for prvek_listu in text:  
    delka_prvku.append(len(prvek_listu))
# tiskne sloupcovy graf a zarovnava pod sebe
odsazeni = 0
for i in range (1, max(delka_prvku) + 1):
    if i < 10:
        odsazeni = 1
    else:
        odsazeni = 0 
    print(i, " " * odsazeni, "|", delka_prvku.count(i) * "*" + "|".rjust(18 - delka_prvku.count(i), " "), delka_prvku.count(i))  