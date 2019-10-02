# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 5
# Date: 02/22/2018
# Title: coinflip
# Description: user enters trial of 5 coins flipping, outputs percentage of heads occured

import random

heads=0
counter=0

ntrials = int(input('How many coin toss trials: '))

for t in range(ntrials):
    Richard_Truong1 = random.randint(0,1)
    Richard_Truong2 = random.randint(0,1)
    Richard_Truong3 = random.randint(0,1)
    Richard_Truong4 = random.randint(0,1)
    Richard_Truong5 = random.randint(0,1)

if Richard_Truong1 + Richard_Truong2 + Richard_Truong3 + Richard_Truong4 + Richard_Truong5 == 5:
    counter=heads+1

percentage = (counter/ntrials)*100

print('Percentage difference ', percentage, '%')

##How many coin toss trials: 10
##Percentage difference 0%

##How many coin toss trials: 100000
##Percentage difference 3.167%

##How many coin toss trials: 5000000
##Percentage difference 3.1222%
