import random
import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist())) # Remove Empty/Duplicates Values
    pass

def run():
    data_from_file: object = file_to_list('nouns.txt') 
    print(data_from_file)

if __name__ == "__main__":
    run()