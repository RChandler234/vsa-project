# REVIEW: Conditionals, for loops, lists, and functions

#INSTRUCTIONS:

#PartI:

#Make the string "sentence_string" into a list called "sentence_list"
#Use a for loop and an append function like this: list.append(something)

sentence_string = "Hello, my name is Monty Python."
sentence_list=[]
sentence_len=len(sentence_string)
for number in sentence_string:
    sentence_list.append(number)

#PartII:
# Print every item of the list using a for loop

for order in range (0, sentence_len):
    print sentence_list[order]


#PartIII:
# write a for loop to find the index of 'b' in the list "vowels"
vowels = ['a', 'b', 'i', 'o', 'u', 'y']
index=0
for place in vowels:
    if place=="b":
        print index
    index=index+1



#PartIV:
# use the index found above to change 'b' to 'e'
vowels[1]="e"

print vowels
#PartV:
# Using a for statement and an if statement, print all the vowels from the sentence
for stuff in sentence_string:
    if stuff in vowels:
        print stuff


#PartVI:
#Make a new function called "vowelFinder" that will return a list that holds all the vowels found in a list (no duplicates).
#The function's parameters should be "list" and "vowels."
def vowelFinder(lst,vowels):
    vlist=[]
    for things in lst:
        if things in vowels:
            vlist.append(things)
    return vlist

vowelList= vowelFinder(sentence_string, vowels)

print vowelList