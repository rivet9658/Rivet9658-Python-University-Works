#練習8-例題3
lst=[]
for i in range(1,10):
    str=input()
    lst.append(str)

for k in range(1,10):
    if k%3 !=0:
        print("|"+lst[k-1].ljust(15)+"|",end="")
    else:
        print("|"+lst[k-1].ljust(15)+"|")
