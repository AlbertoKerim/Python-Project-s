#Program that calculates the first 1000 digits of number e

from math import factorial
from decimal import Decimal,getcontext

n = 10000
start_num = 0    #Because we cant factor number 0

getcontext().prec = n  #Setting the precision to n decimal points

def euler():
    euler_number = Decimal(0)

    for num in range (0,n):
        if num == 1:
            euler_number = euler_number + Decimal(start_num)
            pass

        euler_number = euler_number + (Decimal(1)/Decimal(factorial(num)))

    return euler_number

euler_number = euler()

print(euler_number)












