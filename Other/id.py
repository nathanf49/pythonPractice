#!/usr/bin/python
class identification: #to take in a person's infomation and perform checks
	def __init__ (self,first,last,gender,bday): #reads in data
		self.firstName = first
		self.lastName = last
		self.birthday = bday
		self.gender = gender

	def printID(self): #prints ID
		print(self.firstName, self.lastName)
		print(self.gender)
		print(self.birthday)

def genderInputCheck(gender): #function to check gender input for male/female/other
	if gender == 'Male' or 'M' or 'm' or 'male' or 'MALE':
		return('Male')
	elif gender == 'Female' or 'F' or 'f' or 'female' or 'FEMALE':
		return('Female')
	else:
		return('Other')

def birthdayInputCheck(birthday): #function to check that birthday was input correctly
	if birthday[2] != '/':
		raise SyntaxError('Month input wrong. Please check birthday')
	elif birthday[5] != '/':
		raise SyntaxError('Day input wrong. Please check birthday')
	elif len(birthday) != 10:
		raise SyntaxError('Year input wrong. Please check birthday')
	else:
		return(birthday)

first = input("What's your first name? ")
last = input("What's your last name? ")
gender = input('What is your gender? ')
checked_gender = genderInputCheck(gender)
birthdate = input('Please input your birthday in MM/DD/YYYY format ')
checked_birthday = birthdayInputCheck(birthdate)

person = identification(first, last, checked_gender, checked_birthday)
person.printID()
