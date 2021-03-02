#質數加總
i=eval(input("put a number:"))
e=eval(input("put a number:"))
total=0
y=0
for k in  range(i,e+1):
    for x in range(2,k+1):
        if k%x ==0 and x!=k:
            break
        elif k%x ==0 and x==k:
            total=total+k
            if y==0:
                print(i,"到",e,"之間的質數有:",k,end="")
                y=y+1
            else:
                print(",",k,end="")
                
print(",","加總為",total)
