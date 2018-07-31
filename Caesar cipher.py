print ('What would zou like to do with text:\n1.Encode\n2.Decode')

alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

while True:
    choice = float(input('Choice:'))
    if int(choice) == choice and choice>0 and choice<3:
        choice = int(choice)
        break
    else:
        print(f'Please enter again')


#Encode
if choice == 1:
    while True:
        type_of_encoding = float(input('\nType of encode (3-...):'))
        if int(type_of_encoding) == type_of_encoding and type_of_encoding > 2:
            type_of_encoding = int(type_of_encoding)
            break
        else:
            print(f'Please enter again')

    sentence = input ('\nEnter a sentence: ')
    sentence = sentence.lower()

    list_of_words = sentence.split(' ')
    encoded = []

    for word in list_of_words:
        for letter in word:
            num = 0
            num = alphabet[letter]
            num = num + type_of_encoding
            while num > 26:
                num = num - 26
            let = {v:k for k, v in alphabet.items()}[num]
            encoded.append(let)

        encoded.append(' ')
    print('')
    print('Encoded:')
    for letter in encoded:
        print(letter,end='')

#Decode
if choice == 2:
    while True:
        type_of_encoding = float(input('\nType of encode (3-...):'))
        if int(type_of_encoding) == type_of_encoding and type_of_encoding > 2:
            type_of_encoding = int(type_of_encoding)
            break
        else:
            print(f'Please enter again')

    sentence = input ('\nEnter a sentence: ')

    sentence = sentence.lower()
    list_of_words = sentence.split(' ')
    encoded = []

    for word in list_of_words:
        for letter in word:
            num = 0
            num = alphabet[letter]
            num = num - type_of_encoding
            while num > 26 or num<0:
                num = num + 26
            let = {v:k for k, v in alphabet.items()}[num]
            encoded.append(let)

        encoded.append(' ')
    print('')
    print('Decoded:')
    for letter in encoded:
        print(letter,end='')









