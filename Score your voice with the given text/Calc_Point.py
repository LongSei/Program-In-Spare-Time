import os 
import filecmp
from difflib import Differ

def convert_to_list(filename): 
	with open(filename,'r') as f:
		listl=[]
		for word in f:
			words = word.split()
			for i in words: 
				ip = i.lower()
				listl = listl + [ip]
		return(listl)
numberwrong = 0
f1 = convert_to_list('recorded_text.txt')
f2 = convert_to_list('text_file.txt')
lent = 0
if len(f1) != len(f2): 
	lent = min(len(f1),len(f2))
	numberwrong = max(len(f1), len(f2)) - lent
else:
	lent = len(f1)
for i in range(0, lent): 
	if f1[i] != f2[i]: 
		numberwrong = numberwrong + 1
maxi = max(len(f1), len(f2))
f1 = open("score.txt", "w")
sstr = str(100 * (1 - (numberwrong / (maxi)))) + "%"
f1.write(sstr)
f1.close()
os.system('python3 Score_GUI.py')