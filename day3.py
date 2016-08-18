#30 Days of Code Challenge
#Day 3: Intro to Conditional Statements

#!/bin/python3

import sys


N = int(input().strip())
if N%2>0:
    print('Weird')
elif N>1 and N<6:
    print('Not Weird')
elif N>20:
    print('Not Weird')
else:
    print('Weird')
