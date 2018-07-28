from math import factorial   #We imported factorial because we will need it
from decimal import getcontext, Decimal

while True:
    dec_points = float (input('How much decimal points of pi do you want to get:'))
    if dec_points == int(dec_points):
        dec_points = int(dec_points)
        break
    else:
        print('Please enter again')

getcontext().prec = dec_points  #Set the precision to your own

def pi():
    '''
    Function for calculating pi with the Bailey–Borwein–Plouffe formula
    :return: number pi
    '''

    pi = Decimal(0)

    for n in range (dec_points):
        part1 = ((Decimal(4)/(Decimal(1)+Decimal(8*n)))-
             (Decimal(2)/(Decimal(4)+Decimal(8*n)))-
             (Decimal(1)/(Decimal(5)+Decimal(8*n)))-
             (Decimal(1)/(Decimal(6)+Decimal(8*n))))

        part2 = part1 * (Decimal(1/16)**Decimal(n))

        pi += part2

    return pi

number_pi = pi()
number_pi = str(number_pi)


f = open('Number Pi.txt','w')
f.write(number_pi)
f.close()