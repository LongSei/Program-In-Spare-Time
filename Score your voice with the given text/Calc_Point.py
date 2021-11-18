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
def main():
	numberwrong = 0
	f1 = convert_to_list('recorded_text.txt')
	f2 = convert_to_list('test.txt')
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
	print("Your point is: " + str(100 * (1 - (numberwrong / (maxi)))) + "%")