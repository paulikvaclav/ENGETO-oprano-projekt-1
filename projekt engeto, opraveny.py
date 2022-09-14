
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Vaclav Paulik
# email: paulikvaclav@seznam.cz
# discord: Vasek.P#5176

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
'''.'The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present'''
]


oddelovac = "-"

user = {"bob": "123", "ann": "pass123", "mike": "123", "liz": "pass123"}
username = input("Registrovany uzivatel:")
password = input('Heslo:')



if user.get(username) == password:
    print((f"Vitame te,{username}\nMas na vyber ze 3 textu v aplikaci!"""))
else:
    print("Vase udaje se neschoduji!")

print(oddelovac*45)

vyber = input("Zadej cislo textu 1-3:")
if vyber.isdigit()  in range(1, 4):
    print("Tento text je v nabidce!")

else:

    print("Jinou možnost nenabizime!")


    quit()
print(oddelovac*45)

dohromadyslov = 0
prvnipismeno = 0
velkapismena = 0
malapismena = 0
cislo = 0
listcisel = list()
soucet_cisel = 0

delky_slov = {}
vvyskyt_slov = {}

for slovo in TEXTS[int(vyber)-1].split():
    dohromadyslov = dohromadyslov + 1
    if slovo in delky_slov:

        delky_slov[slovo]=len(slovo)


    if slovo.istitle():
        prvnipismeno = prvnipismeno + 1
    elif slovo.isupper():
        velkapismena = velkapismena + 1
    elif slovo.islower():
        malapismena = malapismena + 1
    elif slovo.isnumeric():
        cislo = cislo + 1
        listcisel.append(int(slovo))

for soucet in listcisel:
    soucet_cisel += int(soucet)


print(f"Soucet slov je: {dohromadyslov}")
print(f"Pocet slov zacinajici velkym pismenem: {prvnipismeno}")
print(f"Pocet slov s velkymi pismeny: {velkapismena}")
print(f"Pocet slov s malymi pismeny: {malapismena}")
print(f"Pocet ciselnych slov je: {cislo}")

print(f"Soucet cisel je:{soucet_cisel}")

print(oddelovac*45)



print("LEN|" + "\t" + "OCCURENCES" + "\t" + "|NR.")

print(oddelovac*25)






dohromadyslov = dict()
for slovo in TEXTS[int(vyber) - 1].split():
    slovo = slovo.rstrip(",.:;")
    delka = len(slovo)
    if delka not in dohromadyslov:
       dohromadyslov[delka] = 0

    dohromadyslov[delka] += 1

for razeni, hodnota in enumerate(dohromadyslov.values()):
    print(f"{(razeni + 1):3}| {'*' * hodnota:15}|{hodnota:1}")

print("-"*25)













