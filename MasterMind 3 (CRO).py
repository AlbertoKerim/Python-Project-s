from random import *

print ('\nDobrodosli u igru Mastermind. Ukratko, cilj ove igre je da vi pogodite 4 nasumicno odabrana znaka \nod mogucih 6 i da pogodite njihova tocna mjesta')

odabrani = []
moji_odabrani = []
crni=0
bijeli=0
br_pokusaja=1
redni=1
n=1

while True:
    moguci_znakovi = input('\nMolimo unesite tocno 6 znakova koje bi ste htjeli u igrici: ')
    if len(moguci_znakovi) == 6:
        break
    else:
        print('Molimo upisite ponovo')


for i in range (1,5):
    odabrani.append(choice(moguci_znakovi))



print('\nNasumicno su odabrana 4 znakova, mozes pogadati izmedu znakova: ', moguci_znakovi)

while True:
    while n<100000000000:
        znak = input(f'\nUpisi {redni}. znak:')
        if len(znak)>1:
            print('Unesi ponovo')
        else:
            break

    redni = redni + 1
    if redni==5:
        redni=1

    while n<100000000000000000:
        index = float(input('Na kojem mjestu je taj znak:'))
        if index == int(index):
            index = int(index)
            index = index-1
            break
        else:
            print('Molimo upisite ponovo')


    moji_odabrani.insert(index,znak)

    print(moji_odabrani)#######

    if len(moji_odabrani) == 4:

        if moji_odabrani == odabrani:
            print (f'\nBravo, pogodio si poredak iz {br_pokusaja}. pokusaja')
            break

        else:

            if moji_odabrani[0] == odabrani[0]:
                crni = crni + 1

            elif moji_odabrani[0] in odabrani:
                bijeli = bijeli + 1

            if moji_odabrani[1] == odabrani[1]:
                crni = crni + 1

            elif moji_odabrani[1] in odabrani:
                bijeli = bijeli + 1

            if moji_odabrani[2] == odabrani[2]:
                crni = crni + 1

            elif moji_odabrani[2] in odabrani:
                bijeli = bijeli + 1

            if moji_odabrani[3] == odabrani[3]:
                crni = crni + 1

            elif moji_odabrani[3] in odabrani:
                bijeli = bijeli + 1

            print (f'\nTrenutni rezultat:\t{crni} crnih\t\t{bijeli} bijelih')

            moji_odabrani = []
            br_pokusaja = br_pokusaja + 1