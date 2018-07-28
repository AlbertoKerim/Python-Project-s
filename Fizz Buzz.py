#Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of
# the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print
#“FizzBuzz”.

for n in range(1,100):

    if n%3 == 0 and n%5 == 0:
        print('Fizz Buzz')
        continue

    if n%3 == 0:
        print('Fizz')
        continue

    if n%5 == 0:
        print('Buzz')
        continue

    print(n)
