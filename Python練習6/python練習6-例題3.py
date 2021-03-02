#練習6-例題3
import random
randlst=[]

def main(randlst):
    count=1
    while count<=100:
        randNum=random.randint(1,1000)
        if randNum not in randlst:
            randlst.append(randNum)
            count+=1
    return randlst

def maxAndmin(randlst):
    randlst.sort()
    for j in range(1,101):
        if j % 10 ==0:
            print("%4d"%(randlst[j-1]))
        else:
            print("%4d"%(randlst[j-1]),end="")
    print()
    randlst.pop(99)
    print(max(randlst))
    randlst.reverse()
    randlst.pop(98)
    print(min(randlst))

main(randlst)
maxAndmin(randlst)
