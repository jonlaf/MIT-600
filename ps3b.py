from ps3a import *
import time
from perm import *
HAND_SIZE = 7
#
#
# Problem #6A: Computer chooses a word
#
#

def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    hi_score = 0
    hi_word = ""
    perm_list=[]
    for i in range(1, HAND_SIZE):
        perm_list += get_perms(hand, i)
    for perm in perm_list:
        if is_valid_word(perm, hand, word_list):
            f = get_word_score(perm, HAND_SIZE)
            if f >= hi_score:
                hi_score = f
                hi_word = perm
    return hi_word
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    total_score = 0
    played_word = "empty"
    while True:
        display_hand(hand)
        played_word = comp_choose_word(hand, word_list)
        if played_word == "":
            break
        print "computer plays '" + played_word + "'."
        total_score += get_word_score(played_word, HAND_SIZE)
        hand = update_hand(hand, played_word)
        print "for a total score of: " + str(total_score) + "."

##structure to facilitate Problem 6C part 2
        
def choose_player(hand, word_list):
    """
    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.
    """
    player_choice = ''
    while player_choice == '':
        player_choice = raw_input("enter 'u' for user played hand. 'c' for the computer to attempt. ").lower()
        if player_choice == 'u':
            play_hand(hand, word_list)
            break
        elif player_choice == 'c':
            comp_play_hand(hand, word_list)
            break
        else:
            print "please enter 'u' or 'c'"
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    NUM_HANDS = 5
    hand = deal_hand(HAND_SIZE)
    while NUM_HANDS > 0:
        choice = raw_input("for new hand enter 'n'. to replay hand enter 'r'. to exit enter 'e'").lower()
        if choice == 'n':
            hand = deal_hand(HAND_SIZE)
            choose_player(hand, word_list)
            NUM_HANDS -= 1
            print str(NUM_HANDS) + " hand(s) remain."
        elif choice == 'r':
            choose_player(hand, word_list)
            NUM_HANDS -= 1
            print str(NUM_HANDS) + " hand(s) remain."
        elif choice == 'e':
            break
        else:
            print "please enter 'n', 'r', or 'e'."
    print "game over"

#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
