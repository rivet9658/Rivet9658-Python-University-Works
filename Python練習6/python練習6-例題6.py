#練習6-例題6
aa=eval(input())
bb=eval(input())
def compute(a,b):
    Armstrongnumbers=[]
    for i in range(a,b+1):
        s=0
        n=len(str(i))
        temp=i
        while temp>0:
            digit = temp % 10
            s += digit ** n
            temp //= 10
        if i == s:
            Armstrongnumbers.append(i)
    print(Armstrongnumbers)
compute(aa,bb)
