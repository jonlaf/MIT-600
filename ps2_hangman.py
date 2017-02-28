# 6.00 Problem Set 3
# 
# Hangman
#
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
# your code begins here!

def pop_remaining(strng, guess):
    """
    strng = remaining (string): list of unguessed letters
    guess = guess (string with length of 1)
    Returns the string of remaining letters after removing the guess letter.
    """
    counter = 0
    newstrng = ""
    for counter in range(0 , len(strng)):
        if str(strng[counter]) == guess:
            newstrng = strng.replace(strng[counter], "")
    return newstrng

def word_search(word, wordblanks, guess):
    """
    word = word(string) the hangman solution word
    wordblanks = wordblanks(string) correct guesses so far, blanks represented by "_"
    guess = string length 1, the letter being guessed
    returns = new wordblanks with correctly guessed letters added or unchanged.
    """
    counter = 0
    newwordblanks = ''
    for counter in range(0, len(word)):
            if str(word[counter]) == guess:
                newwordblanks += guess
            else:
                newwordblanks += wordblanks[counter]
    return newwordblanks

wordlist = load_words()
remaining = 'abcdefghijklmnopqrstuvwxyz_'
guesses = 8
correct = False
print "Hey you! YES YOU!!!! At the keyboard...I'm talking to you! Listen up! I'm trapped in this computer and the only way I can get out is if you beat me at hangman...Please, do your best and you will be handsomely rewarded upon my return to the world of flesh."
word = choose_word(wordlist)
print "I'm thinking of a word that is " + str(len(word)) + " letters long. I'll give you 8 guesses."
wordblanks = ''
newwordblanks = ''
wordblanks_counter = 0
for wordblanks_counter in range(0, len(word)):
    wordblanks += '_'
while guesses > 0 and wordblanks != word:
    print str(guesses) + " guesses remain."
    print "Letters Remaining: " + remaining[:-1]
    print wordblanks
    guess = str(raw_input("Guess a letter: "))
    print "Hmmm..." + guess + ", huh?"
    guess.lower()
    if guess.isalpha() == False or len(guess) > 1:
        print "Will you please take this seriously? You have to guess A LETTER!"
    else:
        newwordblanks = word_search(word, wordblanks, guess)
        remaining = pop_remaining(remaining, guess)
        if newwordblanks != wordblanks:
            print "You got one!"
            wordblanks = newwordblanks
        else:
            guesses -= 1
            print "That letter is not in the word..."

if guesses == 0:
    print "You lose "
if word == wordblanks:
    print "I'm FREEEEEEEEEEEE HAHAHAHA MUAHAHAHAHAA!!! Now it is your turn! Now it is YOU who shall turn the electrical cranks within this machine until someone can best YOU at a game of HangmanTM"

          







