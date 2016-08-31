#30 days of code challenge
#Day 9: Recursion

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return (factorial(N-1)*N)
    
N = int(input().strip())
print(factorial(N))
