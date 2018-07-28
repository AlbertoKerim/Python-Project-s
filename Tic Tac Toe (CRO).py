def pobjednik(lista):
    if lista[0] == lista[1] == lista[2] and lista[0] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[3] == lista[4] == lista[5]and lista[3] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[6] == lista[7] == lista[8] and lista[6] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[0] == lista[3] == lista[6] and lista[0] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[1] == lista[4] == lista[7] and lista[1] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[2] == lista[5] == lista[8] and lista[2] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[0] == lista[4] == lista[8] and lista[0] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[2] == lista[4] == lista[6] and lista[2] == 'X':
        print('\nBravo, igrac X je pobijedio')
        return True
    elif lista[0] == lista[1] == lista[2] and lista[0] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[3] == lista[4] == lista[5]and lista[3] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[6] == lista[7] == lista[8] and lista[6] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[0] == lista[3] == lista[6] and lista[0] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[1] == lista[4] == lista[7] and lista[1] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[2] == lista[5] == lista[8] and lista[2] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[0] == lista[4] == lista[8] and lista[0] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True
    elif lista[2] == lista[4] == lista[6] and lista[2] == 'O':
        print('\nBravo, igrac O je pobijedio')
        return True

def ploca(lista):

    print('\n' * 100)

    print(f'{lista[0]} | {lista[1]} | {lista[2]}')
    print(f'{lista[3]} | {lista[4]} | {lista[5]}')
    print(f'{lista[6]} | {lista[7]} | {lista[8]}')

    pobjednik(lista)

def igra():
    odigrano = []
    brojac = 1
    igrac = 1
    lista = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    while True:
        igrac = igrac + 1
        if igrac%2 == 0:
            print('\nIgrac X')
        else:
            print('\nIgrac O')

        while True:
            broj=float(input('\nUpisi poziciju:'))
            if broj == int(broj):
                broj = int(broj)
                break
            elif broj == None:
                print('Krivo upisano, molimo unesite ponovo')
            else:
                print('Krivo upisano, molimo unesite ponovo')

        broj2 = broj - 1



        if igrac%2 == 0:
            lista[broj2] = 'X'

        else:
            lista[broj2] = '0'

        ploca(lista)

        if pobjednik(lista) == True:
            break

        if brojac == 9 and pobjednik(lista) != True:
            print('Izjednaceno')
            break

        brojac = brojac + 1


def main():
    igra()
    odabir = input('\nHoces li igrati jos(Yes/No):')
    while True:
        if odabir.lower() == 'yes':
            igra()
        elif odabir.lower() == 'no':
            break
        else:
            print('\nKrivo upisano')

main()

