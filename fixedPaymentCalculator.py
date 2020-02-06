# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:`30:48 2020

@author: Nathan
"""
def interestCalculator(balance, annualInterestRate, minimumMonthlyPayment):
    monthlyInterestRate = annualInterestRate / 12 #calculate interest by month instead of year
    monthlyUnpaidBalance = balance - minimumMonthlyPayment #solves for balance after min payment
    return(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)) #calculates and returns new balance

balance = 4773
annualInterestRate = 0.2
minimumMonthlyPayment = 10 #start payment at 10
currentBalance = balance #set a variable to balance that can be changed without losing balance
while currentBalance > 0:
    for x in range(1,13):
        currentBalance = interestCalculator(currentBalance, annualInterestRate, minimumMonthlyPayment) #saves output of calculator as new blanace
    if currentBalance > 0: #if balance is not paid off
        currentBalance = balance #reset balance
        minimumMonthlyPayment += 10 #increase payment by 10
print('Lowest Payment: ', minimumMonthlyPayment)

'''
 Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310

 Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440
 Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
'''