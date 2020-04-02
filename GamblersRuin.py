import random
import matplotlib.pyplot as plt

#While loop adds $1 to balance for every 1 int and subtracts $1 for ever 2 int
#Simulation is run 100 times and prints coin flips performed

balance = 5
balanceHist = []
coinFlips = 0
coinFlipsHist = []
for trialNumber in range(100):
    while(balance > 0):
        flipResult = random.randint(1,2)
        if(flipResult == 1):
            balance += 1
            balanceHist.append(balance)
        else:
            balance -= 1
            balanceHist.append(balance)
        coinFlips += 1
        coinFlipsHist.append(coinFlips)
            
    
print('Toal number of coin flips: ' + str(coinFlips))

plt.scatter(coinFlipsHist, balanceHist)
plt.title('Distribution of Coinflips vs Balance')
plt.ylabel('Balance')
plt.xlabel('Coinflips') 
