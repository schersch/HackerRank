#30 Days of Code Challenge
#Day 6: Let's Review


t = 0
t = int(input().split()[0])
s = []
o = [' ']

for i in range(t):
    s = list(input())
    #print(s)
    for j in range(len(s)):
        #print(o)
        if j%2>0:
            o.append(s[j])
        else:
            o.insert(int(j/2),s[j])
    print(''.join(o))
    o = [' ']
    
