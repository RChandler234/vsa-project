# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""


a= int(raw_input("How many Fibonacci numbers to generate?: "))
x=1
for number in (1,a+1):
    FN=number+x+(y-x)
    x=y
    y=FN
print FN