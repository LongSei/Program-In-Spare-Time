import random
import docx

file_word_use_for = "" #path

def get_list_definition_and_list_word(filename): 
	list_definition = []
	list_word = []
	list_couple_word_and_define = []
	doc = docx.Document(filename)
	for para in doc.paragraphs: 
		list_couple_word_and_define.append(para.text)
	for couple in list_couple_word_and_define: 
		definition = ""
		word = ""
		isok = False
		afterisok = False
		for charc in couple: 
			if charc == ':':
				isok = True
			else: 
				if isok == True: 
					if afterisok == False: 
						afterisok = True
						continue
					definition = definition + charc
		for charc in couple: 
			if charc == ':': 
				break
			else: 
				word = word + charc

		list_definition.append(definition.upper())
		list_word.append(word.upper())

	# Optimize for list_word
	for i in range(0, len(list_word)): 
		new_word = ""
		ok = False
		for charc in list_word[i]: 
			if charc != " ": 
				ok = True
				new_word = new_word + charc
			else: 
				if ok == False: 
					continue
				else: 
					new_word = new_word + charc
		list_word[i] = new_word
	for i in range(len(list_word) - 1, -1, -1): 
		new_word = ""
		ok = False
		for charc in list_word[i]: 
			if charc != " ": 
				ok = True
				new_word = new_word + charc
			else: 
				if ok == False: 
					continue
				else: 
					new_word = new_word + charc
		list_word[i] = new_word

	# Optimize for list_definition
	for i in range(0, len(list_definition)): 
		new_word = ""
		ok = False
		for charc in list_definition[i]: 
			if charc != " ": 
				ok = True
				new_word = new_word + charc
			else: 
				if ok == False: 
					continue
				else: 
					new_word = new_word + charc
		list_definition[i] = new_word
	for i in range(len(list_definition) - 1, -1, -1): 
		new_word = ""
		ok = False
		for charc in list_definition[i]: 
			if charc != " ": 
				ok = True
				new_word = new_word + charc
			else: 
				if ok == False: 
					continue
				else: 
					new_word = new_word + charc
		list_definition[i] = new_word
	return [list_word, list_definition]

def optimize_list(word, define):
    isok = False
    while isok == False:
        remain = False
        index1 = -1
        index2 = -1
        for position1 in range(0, len(word)): 
            for position2 in range(0, len(word)): 
                if position1 == position2: 
                    continue
                elif word[position1] == word[position2]: 
                   remain = True
                   index2 = position2
                   index1 = position1
        if index1 != -1 and index2 != -1:
            define[index1] = define[index1] + ', ' + define[index2]
            define.pop(index2)
            word.pop(index2)
        if remain == True: 
            isok = False
        else: 
            isok = True
    return [word, define]

def result_optimize(): 
    couple_file = get_list_definition_and_list_word(file_word_use_for)
    op_couple = optimize_list(couple_file[0], couple_file[1])
    words = op_couple[0]
    defines = op_couple[1]
    return [words, defines]

def running(): 
    words = result_optimize()[0]
    defines = result_optimize()[1]
    while True:
        print("(If you want to exit the program, type <!quit>, else input your key: ")
        prefix = str(input())
        if prefix == "!quit": 
            break
        prefix = prefix.upper()
        for i in range(0, len(words)): 
            word = words[i]
            if prefix in word: 
                print(word + ": " + defines[i])

if __name__ == '__main__': 
    running()
