# Name: Reid Chandler
# Date: 6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name=raw_input("Enter your name: ")
age= int(raw_input("Enter your age: "))
stat= " will turn 100 in the year "
Bday=raw_input("Have you had your birthday this year yet?: ")
Bbday=Bday.lower()
print Bday
if Bday == "yes" or "Yes":
    yrs= 100-age
else:
    yrs= 99-age
Fut= str(yrs+2017)
first_letter = name[0].upper()
other_letters = name[1:].lower()

Name= first_letter+other_letters


print Name+stat+Fut
