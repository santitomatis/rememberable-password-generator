import random
import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values
	

def run():
	nouns: object = file_to_list('nouns.txt') 
	# print(nouns[])
if __name__ == "__main__":
	run()