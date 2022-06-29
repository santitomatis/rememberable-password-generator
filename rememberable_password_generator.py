import random
import pandas as pd
import string

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values

def password_generator(nouns, amount_words, spaces, case):
	password = []
	CHARS = ('*', '+', '-', '/', '_', '!', ',', ';', '.', '>', '<', '~', '&')
	CASES = ("uc", "lc", "c")
	char = " "

	if spaces == "y":
		char = random.choice(CHARS)
	
	if case == "r":
		case = random.choice(CASES)

	j = 0
	for i in range(amount_words):
		word = random.choice(nouns)
		password.append(word)
		if i != amount_words - 1:
			password.append(char)
		
		# if i != amount_words - 1 and i != 0:
		if i != 0:
			j = j + 1
		
		if case == "uc":
			password[j] = password[j].upper
		
		elif case == "lc":
			password[j] = password[j].lower

		elif case == "c":
			password[j] = password[j].capitalize
	
		j = j + 1

	password = "".join(password)
	return password
			

def run():
	nouns: object = file_to_list('nouns.txt') 
	menu_case = """
		Do you want your password to be:
		-uc (uppercase)
		-lc (lowercase)
		-c (capitalized)
		-r (random)
		(Just type uc; lc; c or r according to your choice)
		"""
	print("Welcome to The Rememberable Password Generator Project") 
	advanced_config = str(input("Do you want to do some advanced configuration? Just type y/n (yes or no) "))
	if advanced_config == "y":
		amount_words = int(input("How many words do you want your password to have? (recommended: 3) "))
		spaces = str(input("Do you want to separate the words with a random char (eg: _ ; -)? Just type y/n (yes or no) Words will be separated with spaces by default "))
		case = str(input(menu_case))

	elif advanced_config == "n":
		amount_words = 3
		spaces = " "
		case = "r"

	password = password_generator(nouns, amount_words, spaces, case)
	print("Your password is:")
	print(password)

if __name__ == "__main__":
	run()