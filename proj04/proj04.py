# Name:Reid Chandler
# Date:6/20/17

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""


user= raw_input("Write a string: ")
user_input=user
user=user.lower()
user_list= []
reverse_list=[]
user=user.replace(" ","")
for letter in user:
    user_list.append(letter)
    mylist=user_list
x= len(user_list)
for letter in range (1,x+1):
    reverse_list.append(user_list[-1])
    user_list= user_list[:-1]
user_input=user_input[0].upper()+user_input[1:].lower()
if mylist==reverse_list:
    print user_input , "is a palindrome."
else:
    print user_input, "is not a palindrome."