# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:37:26 2020

@author: Nathan
"""

def interestCalculator(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12 #calculate interest by month instead of year
    minimumMonthlyPayment = monthlyPaymentRate * balance #solves for min payment per month
    monthlyUnpaidBalance = balance - minimumMonthlyPayment #solves for balance after min payment
    return(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)) #calculates and returns new balance

balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = .01
for x in range(1,13):
    balance = interestCalculator(balance, annualInterestRate, monthlyPaymentRate) #saves output of calculator as new blanace
    print('Month ', x, ' remaining balance: ', balance)
print('Remaining balance: ', round(balance,2))