#30 days of code challenge
#Day 8: Dictionaries and Maps

phoneBook = {}
N = 0
newitem = ''

N = int(input().strip())
for i in range(N):
    newitem = input().split()
    phoneBook[newitem[0]] = int(newitem[1])

try:
    q = input().strip()
except:
    q = None

while q is not None:
    try:
        print(q+"="+str(phoneBook[q]))
    except:
        print("Not found")
    try:
        q = input().strip()
    except:
        q = None
