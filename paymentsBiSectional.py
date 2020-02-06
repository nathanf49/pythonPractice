# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:18:12 2020

@author: Nathan
"""

def interestCalculator(balance, monthlyInterestRate, minimumMonthlyPayment):
    monthlyUnpaidBalance = balance - minimumMonthlyPayment #solves for balance after min payment
    return(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)) #calculates and returns new balance

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12 #calculate interest by month instead of year
lowBound = balance/12
highBound = (balance * ((1 + monthlyInterestRate) ** 12))/12
currentBalance = balance #set a variable to balance that can be changed without losing balance
while abs(currentBalance) > 0.01: #checks if absolute value of currentBalance is greater than 1 cent (goal accuaracy)
    minimumMonthlyPayment = (lowBound + highBound)/2
    for x in range(1,13):
        currentBalance = interestCalculator(currentBalance, monthlyInterestRate, minimumMonthlyPayment) #saves output of calculator as new blanace
    if currentBalance > 0.01: #didn't pay enough, increase low bound
        lowBound = minimumMonthlyPayment
    elif currentBalance < 0.01: #paid too much, lower high bound
        highBound = minimumMonthlyPayment
    if abs(currentBalance) > 0.01:
        currentBalance = balance #reset balance
print('Lowest Payment', round(minimumMonthlyPayment,2))
        