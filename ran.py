import random
randomlist=[]


while len(randomlist) < 6:
    n= random.randint(1,49)
    if n not in randomlist:
        randomlist.append(n)
randomlist.sort()
print(randomlist)