# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Gambler's Ruin

import random

#while loop adds $1 to balance for every 1 int and subtracts $1 for ever 2 int
#Simulation is run 100 times and prints coin flips performed

listofNumberFlips = []
for trialNumber in range(100):
    balance = 3
    coinFlips = 0
    while(balance > 0):
        flipResult = random.randint(1,2)
        if(flipResult == 1):
            balance += 1
        else:
            balance -= 1
        coinFlips += 1
    print('Total simulations run: ' + str(trialNumber))
    print('Toal number of coin flips: ' + str(coinFlips))
    listofNumberFlips.append(coinFlips)

"""
Max number of coin flips overserved: 2043
Minimum number of coin flips observed: 3
"""
