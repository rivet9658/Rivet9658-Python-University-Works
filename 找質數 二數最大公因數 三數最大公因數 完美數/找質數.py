#找質數
i=eval(input("put a number:"))
e=eval(input("put a number:"))
for k in  range(i,e+1):
    for x in range(2,k+1):
        if k%x ==0 and x!=k:
            break
        elif k%x ==0 and x==k:
            print(k)
