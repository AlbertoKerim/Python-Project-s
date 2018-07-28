from random import randint

list = []

for num in range(1,1000):
    number = randint(1,1000)
    list.append(number)

print(list)



def bubble_sort(list):
    a = 0
    b = 1
    list_len = len(list)

    while True:

        if b == len(list):
            a = 0
            b = 1

        elif list[a] > list[b]:
            list[a], list[b] = list[b], list[a]
            print(list)

        elif list[b]>list[a] or list[b] == list[a]:
            a=a+1
            b=b+1



x = bubble_sort(list)


