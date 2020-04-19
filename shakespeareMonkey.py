#!/usr/bin/python
import random
import string

def generateString():
	letters=string.ascii_lowercase
	return(''.join(random.choice(letters) for x in range(23)))

def score(random):
	string='methinksitislikeaweasel'
	score=0
	for x in range(22):
		if random[x] == string[x]:
			score=score+1
	return(score)
def run():
	highScore=0
	for x in range(100000):
		random=generateString()
		newScore=score(random)
		if newScore > highScore:
			highScore=newScore
	return(highScore)
print(run())
