# Name: Reid Chandler
# Date: 6/20/17

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

"""
#Fibonacci Sequence (For Loop)
x= int(raw_input("How many Fibonacci numbers to generate?: "))
a=0
b=1
for number in range (1,x+1):
    if number== 1:
        FN=a+b
        print FN
    else:
        FN=a+b
        print FN
        a=b
        b=FN
"""
"""
#Fibonacci Sequence (While Loop)
x= int(raw_input("How many Fibonacci numbers do you want?: "))
a=0
b=1
number=1
while number < x+1:
    if number == 1:
        FN=a+b
        print FN
        number=number+1
    else:
        FN=a+b
        print FN
        a=b
        b=FN
        number=number+1
"""
""""
#Powers of 2
x= int(raw_input("How many powers of 2 do you want?: "))

for number in range (1,x+1):
    power= 2 ** number
    print power
"""
#Divisors
x=int(raw_input("What number do you want the divisors of?: "))
for divisor in range (1, x+1):
        z=x%divisor
        if z==0:
            print divisor