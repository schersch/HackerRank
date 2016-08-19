#30 Days of Code Challenge
#Day 7: Arrays

#!/bin/python3

import sys
outs = []

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(n):
    outs.insert(0,arr[i])
print(" ".join(str(j) for j in outs))
