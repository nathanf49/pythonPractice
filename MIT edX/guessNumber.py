# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:03:35 2020

@author: Nathan


Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Important
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
"""

print("Please think of a number between 0 and 100!")
guess = 50
currentRange = [0,100]
response = ''
while response != 'c': #loop breaks when it guesses correctly, this breaks it 1 loop late
    print("Is your secret number " + str(guess))
    
    response = '' #resets response for while loop below
    while response != 'c' and response != 'h' and response != 'l': #makes sure user inputs a valid option
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ") #used for keeping track of the users response to questions
    
    if response == 'h':
        currentRange[1] = guess #makes range lower
    elif response == 'l':
        currentRange[0] = guess #makes range higher
    guess = int((currentRange[0] + currentRange[1]) / 2) #Make new guess as average of range
print('Game over. Your secret number was: ' + str(guess))
    
    
    
