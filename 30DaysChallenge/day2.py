#30 Days of Code Challenge
#Day 2: Operators

mealCost = 0.0
tipPercent = 0
taxPercent = 0
tip = 0.0
tax = 0.0

mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100
totalCost = mealCost + tip + tax

print('The total meal cost is', round(totalCost), 'dollars.')
