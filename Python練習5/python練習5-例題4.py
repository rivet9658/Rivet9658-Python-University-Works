#練習5-例題4
def totalAndmean():
    total=0
    for i in num:
        total=total+i
    return total
def main():
    for j in range(1,11):
        x=eval(input("put number:"))
        num.append(x)
    t=totalAndmean()
    print("sum=",t,"mean=",t/10)
num=[]
main()
