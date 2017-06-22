# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
word=choose_word(wordlist)
word_copy=word
length=len(word)
guessed=[]
lst_word=[]
blank=""
counter=10000
for number in range (1, length+1):
    lst_word.append(word_copy[0])
    word_copy=word_copy[1:]
for stuff in range (1,length+1):
    blank = blank + "_"

def add(letter):
    guessed.append(letter)

an=[]
def correct(ltr, word):
    answer=an
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    for thing in range (0,length):
        if ltr == word[thing]:
            """"
            if answer[thing] in alphabet:
                answer = answer
            else:
             """
            """
            answer=answer+ltr
        else:
            answer = answer + "_"
            """
            an.append(ltr)
    return answer

print "Welcome to Hangman!"
print "I am thinking of a word that is", length, "letters long."
print word
guess=8
while guess !=0 and lst_word !=blank:
    print "You have", guess, "guesses left."
    print "You have guessed:", guessed
    player_g=raw_input("Please guess a letter: ")
    if player_g in lst_word:
        add(player_g)
        print correct(player_g, word)
        counter=counter-1
    else:
        add(player_g)
        guess=guess-1