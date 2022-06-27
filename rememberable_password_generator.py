def run():
	a_file = open("nouns.txt", "r")

	list_of_lists = []
	for line in a_file:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		list_of_lists.append(line_list)

	a_file.close()

	j = 0
	for i in list_of_lists:
		auxiliar = str(list_of_lists[j])
		print(auxiliar)
		auxiliar.replace("[", "")
		auxiliar.replace("]", "") 
		print(auxiliar)
		break
		list_of_lists[j] = auxiliar
		j = j + 1

#test
	print(list_of_lists)

if __name__ == "__main__":
    run()