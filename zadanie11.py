magazyn = [
    {'nazwa': 'mleko', 'cena': 12},
    {'nazwa': 'czekolada', 'cena': 13},
    {'nazwa': 'tyskie', 'cena': 8},
    {'nazwa': 'audi', 'cena': 20000},
]

for pozycja in magazyn:
    print(pozycja['nazwa'])

bug = 'X2X'

if bug in magazyn:
    print("znaleziono {0}".format(bug))
else:
    print("Brak w magazynie {0}".format(bug))
