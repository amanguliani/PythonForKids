from random_word import RandomWords

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def get_a_new_word():
	length = 4
	r = RandomWords()
	word = ''
	while(len(word) !=length or does_contain_repeated_words(word)):
		word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb", minLength=length, maxLength=length)
	return word

def is_input_word_same_length(my_word, guessed_word):
    return len(my_word) == len(guessed_word)

def does_contain_repeated_words(guessed_word):
	return len(set(guessed_word)) != len(guessed_word)

def is_valid_dictionary_word(guessed_word, english_words):
  return guessed_word in english_words
	
	
def is_win(my_word, guessed_word):
	return my_word == guessed_word

def calculate_bulls_and_cows(my_word, guessed_word):
	total_count = len(set(my_word) & set(guessed_word))
	bulls = 0
	for i,j in zip(my_word, guessed_word):
		if (i==j):
			bulls +=1
	return {"Bulls": bulls, "Cows": total_count - bulls}

def game_play(my_word, english_words):
	list_of_guessed_words =[]
	word_not_found = True
	num_of_tries = 0
	while (num_of_tries < 10):
		# take a inout from user
		guessed_word = input("\n" + str(num_of_tries+1) + '. ').lower()
		
		# valid checks
		if(not is_input_word_same_length(my_word, guessed_word)):
			print('Input word is not of the correct length as guessed word, Please guess again')
			continue
		if(does_contain_repeated_words(guessed_word)):
			print('Input word contains repeated characters, Please guess again')
			continue
		if(not is_valid_dictionary_word(guessed_word, english_words)):
			print("Input word is not a valid dictionary word, Please guess again")
			continue

		if(is_win(my_word, guessed_word)):
			print('\n\n\nYou guessed it corectly !!!!!')
			word_not_found = False;
			break

		bulls_cows = calculate_bulls_and_cows(my_word, guessed_word)
		list_of_guessed_words.append(guessed_word)
		num_of_tries +=1
		
		print("Bulls {}, Cows {}".format(bulls_cows["Bulls"], bulls_cows["Cows"]))
		print('You have ' + str(10-num_of_tries) + ' chances left')
		print("You guessed words till now: [" + ','.join(list_of_guessed_words) + "]") 

	if (word_not_found):
		print ('\n\nSorry you couldnt find my word, my word was ' + my_word)

if __name__ == "__main__":
    my_word = get_a_new_word().lower()
    english_words = load_words()
    print('Welcome to Cows and Bulls, a word guessing game !!!')
    quit = input("To play, Press any key to continue, or Q to quit.   ")

    if (quit != 'Q'):
        print('I have selected a four letter word for you to guess, with no repeating characters you get 10 changes to guess my word. Lets begin... !!!\n')
        game_play(my_word, english_words)
        print('Thanks for playing')