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
blank=[]
counter=10000
for number in range (1, length+1):
    lst_word.append(word_copy[0])
    word_copy=word_copy[1:]
for stuff in range (1,length+1):
    blank.append('_')






def add(letter):
    guessed.append(letter)


def correct(ltr, word,an):

    for thing in range (0,length):
        if ltr == word[thing]:
            an[thing]=ltr
    return an

print "Welcome to Hangman!"
print "I am thinking of a word that is", length, "letters long."
guess=8
while guess !=0:
    print "You have", guess, "guesses left."
    print "You have guessed the letters:", guessed
    player_g=raw_input("Please guess a letter: ")
    wrong=correct(player_g, word, blank)
    player_g=player_g.lower()
    if player_g in lst_word:
        add(player_g)
        print "Good guess:", correct(player_g, word,blank)
        if lst_word == correct(player_g, word, blank):
            print "Congratulations, You won. The man lives to hang another day. The word was", word
            break
    else:
        add(player_g)
        guess=guess-1
        print "Sorry, that letter is not in my word:", wrong
        if guess==7:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
        elif guess==6:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0           2"
            print "0           2"
            print "0           2"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
        elif guess==5:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0          32"
            print "0         3 2"
            print "0        3  2"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
        elif guess ==4:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0          323"
            print "0         3 2 3"
            print "0        3  2  3"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
            print "0"
        elif guess==3:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0          323"
            print "0         3 2 3"
            print "0        3  2  3"
            print "0          6"
            print "0         6"
            print "0        6"
            print "0"
            print "0"
            print "0"
        elif guess==2:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0          323"
            print "0         3 2 3"
            print "0        3  2  3"
            print "0          6 6"
            print "0         6   6"
            print "0        6     6"
            print "0"
            print "0"
            print "0"
        elif guess==1:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0          323"
            print "0         3 2 3"
            print "0        3  2  3"
            print "0          6 6"
            print "0         6   6"
            print "0        1     1"
            print "0      __1     1__"
            print "0"
            print "0"
        elif guess==0:
            print "0000000000000"
            print "0           0"
            print "0           1"
            print "0          1 1"
            print "0           1"
            print "0          323"
            print "0         3 2 3"
            print "0        3  2  3"
            print "0          6 6"
            print "0         6   6"
            print "0        1     1"
            print "0      __1     1__"
            print "0"
            print "0          RIP"
if guess ==0:
    print "Sorry, you ran out of guesses. The word was", word, "Better luck next time"