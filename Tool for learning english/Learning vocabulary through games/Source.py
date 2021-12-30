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
	random.shuffle(list_couple_word_and_define)
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

def tell_to_stop(): 
	print("You want to continue: [Y/N]") 
	choose = input().upper()
	if choose[0] == 'Y': 
		return True
	else: 
		return False

# Review vocabulary
def game_0(): 
	list_word_and_definition = get_list_definition_and_list_word(file_word_use_for)
	print("Choose your primary language: " + '\n' + "1: English" + '\n' + "2: Vietnamese")
	language = int(input())
	if language == 1: 
		list_word = list_word_and_definition[0]
		list_definition = list_word_and_definition[1]
	else: 
		list_word = list_word_and_definition[1]
		list_definition = list_word_and_definition[0]

	for i in range(0, len(list_word)):
		word = list_word[i] 
		print("////////////////////////////////////")
		print("Your word: " + word)
		print("1: If you want to skip" + '\n' + "2: To see definition" + '\n' + "3: To exit")
		choose = int(input())
		if choose == 1: 
			print('\n', end = "")
			continue
		elif choose == 2: 
			print("Your definition: " + list_definition[i] + '\n')
		else: 
			return False
	return True

# Find defination of the word
def game_1(): 
	points = 0
	list_word_and_definition = get_list_definition_and_list_word(file_word_use_for)
	list_word = list_word_and_definition[0]
	list_definition = list_word_and_definition[1]
	print("Number of game you want to play: ")
	timer = int(input())
	total = timer
	while timer > 0: 
		timer = timer - 1
		pos = random.randint(0, len(list_word) - 1)
		print("////////////////////////////////////")
		print("Definition: " + list_definition[pos])

		list_word_correct = []
		for i in range(0, len(list_word)): 
			if list_definition[i] == list_definition[pos]: 
				list_word_correct.append(list_word[i]) 
		print("Type your answer, What is this spelled ??")
		word = str(input())
		if word.upper() in list_word_correct: 
			print("You have one more point !!")
			points = points + 1
		else: 
			print("You get wrong answer !!")
		print('\n' + "These words will give you a correct answer: ")
		for words in list_word_correct: 
			print(words, end = " ")
		print('\n\n', end = "")
	print("Your total score is: " + str(points) + "/" + str(total) + '\n')
	return True

# Matching definition and spelling
def game_2(): 
	list_word_and_definition = get_list_definition_and_list_word(file_word_use_for)
	list_word = list_word_and_definition[0]
	list_definition = list_word_and_definition[1]
	print("////////////////////////////////////")
	print("Type number of word you want to play with: ")
	number_word = int(input())
	col_A = list_word[:number_word]
	col_B = list_definition[:number_word]
	random.shuffle(col_B)
	ans = list(zip(col_A, col_B))
	maxi_range = 0
	for i in range(0, number_word): 
		word = ans[i][0]
		define = ans[i][1]
		maxi_range = max(maxi_range, len(word))
	maxi_range = maxi_range + 7
	for i in range(0, number_word): 
		word = col_A[i]
		define = col_B[i]
		middle = maxi_range - len(word)
		print(str(i + 1) + ": " + word + " " * (middle - len(str (i + 1))) + chr(ord("A") + i) + ": " + define)
	print('\n' + "Enter your answers in pairs, for example: 1A 2C 3B")
	answer = str(input())
	trash = []
	word = ""
	for i in answer: 
		if i == " ": 
			continue
		if ord(i) >= 65 and ord(i) <= 90: 
			word = word + i
			trash.append(str(word))
			word = ""
		else: 
			word = word + i		
	answer = trash
	answer = sorted(answer)
	points = 0
	for i in answer: 
		word_id = int(i[:(len(i) - 1)]) - 1
		define_id = ord(i[len(i) - 1]) - ord('A')
		if col_B[define_id] == list_definition[word_id]: 
			points = points + 1
	print("Your points: " + str(points) + "/" + str(number_word))
	print("Right answer:")
	for i in range(0, number_word): 
		print(list_word[i] + ": " + list_definition[i])
	print('\n', end = "")


def start_game(game_id): 
	if game_id == 0: 
		game_0()
		return True
	if game_id == 1: 
		game_1()
		return True
	if game_id == 2: 
		game_2()
		return True
	return False
	

if __name__ == '__main__': 
	while True: 
		print("Choose your game: ")
		print("0: To review all your words")
		print("1: You will have a definition and your mission is find spelling for it")
		print("2: Matching word and defintion")
		print("You can stop this program by type the other number")
		game = int(input())
		if start_game(game) == False: 
			break 
