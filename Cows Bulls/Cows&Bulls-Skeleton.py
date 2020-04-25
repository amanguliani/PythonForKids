#!/usr/bin/env python
from pyenchant import enchant

def get_a_new_word():
	pass

def is_input_word_same_length(my_word, guessed_word):
    pass

def does_contain_repeated_words(guessed_word):
	pass

def is_valid_dictionary_word(guessed_word):
	dictionary = enchant.Dict("en_US")
	return dictionary.check(guessed_word)
	
def is_win(my_word, guessed_word):
	pass

def calculate_bulls_and_cows(my_word, guessed_word):
	pass

def game_play(my_word):
	pass

if __name__ == "__main__":
    my_word = get_a_new_word().lower()
    print('Welcome to Cows and Bulls, a word guessing game !!!')
    quit = input("To play, Press any key to continue, or Q to quit.   ")

    if (quit != 'Q'):
        print('I have selected a four letter word for you to guess, with no repeating characters you get 10 changes to guess my word. Lets begin... !!!\n')
        game_play(my_word)
        print('Thanks for playing')
