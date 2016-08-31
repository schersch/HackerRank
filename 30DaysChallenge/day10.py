#30 days of code challenge
#Day 10: Binary Numbers

#!/bin/python3

import sys


n = int(input().strip())
n = bin(n)
n = n[2:]
count = 0

def bincount(N, current):
    #print(N, current)
    if len(N) < 1:
        return 0
    if len(N)<2:
        if N[0] == '1':
            return 1
        else:
            return 0
    if N.find('1') == -1:
        return current
    if N[N.find('1'):].find('0') == -1:
        nex = len(N) - N.find('1')
    else:
        nex = N[N.find('1'):].find('0')-N.find('1')
    if nex > current:
        current = nex
    if N.find('1') == len(N):
        return current
    else:
        N = N[(N.find('1') + 1):]
        return max(nex, bincount(N,current))
    
print(bincount(n,0))
