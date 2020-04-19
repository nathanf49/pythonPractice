#!/usr/bin/python

class Fraction:
	def __init__(self,top,bottom):
		self.num=top
		self.den=bottom
	def __str__(self):
		return str(self.num)+"/"+str(self.den)

numerator=input("Input a Numerator: ")
denominator=input("Input a Denominaor: ")
myFraction = Fraction(numerator,denominator)
print(myFraction.__str__())

