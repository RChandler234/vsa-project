# Name: Reid Chandler
# Date: 6/21/17

# proj05: functions and lists

# Part I
import random

def divisors(num):
    divisor_list=[]
    for divisor in range(1, num + 1):
        z = num % divisor
        if z == 0:
            divisor_list.append(divisor)
    return divisor_list



def prime(num):
    divisor_list=divisors(num)
    list_length = len(divisor_list)
    if list_length < 3:
        return True
    else:
        return False


# Part II

def intersection(lst1, lst2):
    lst3=[]
    lst4=lst2
    if len(lst1)== 0:
        return []
    elif len(lst2)== 0:
        return []
    else:
        while lst1 != []:
            if len(lst2)== 0:
                lst2 = lst4
                lst1 = lst1[1:]
            elif lst2[0]==lst1[0]:
                lst3.append(lst2[0])
                lst2=lst2[1:]
            elif lst2 != []:
                lst2 = lst2[1:]
        return lst3


    return ["test"]




# Part III

def find_ab(side1, side2, side3):
    """
    Takes three side lengths an returns two smallest in a list
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: list of 2 ints or floats
    """
    return [0, 0]

def find_c(side1, side2, side3):
    """
    Takes three side lengths an returns the largest
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: int or float
    """
    return 0

def square(side):
    """
    Takes a side length and returns the side length squared
    :param side: int or float
    :return: int or float
    """
    return 0

def pythagorean(a,b,c):
    """
    Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: bool
    """
    return False

def is_right(side1, side2, side3):
    """
    Takes three side lengths and returns true if triangle is right
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: bool
    """
    return False

# TESTS
# Feel free to add your own tests as needed!
""""
print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")
"""

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
