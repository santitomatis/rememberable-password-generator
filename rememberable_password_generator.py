import random
import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values

def strip(list):
	stripped_list = []
	# print(len(stripped_list))
	for i in range(len(list)):
		assistant = list[i].replace("'", "")
		stripped_list.append(assistant)
		return stripped_list
	

def run():
	nouns: object = file_to_list('nouns.txt') 
	# print(nouns)
	stripped_nouns: object = strip(nouns)
	print(stripped_nouns)

if __name__ == "__main__":
	run()