#非質數加總
i=eval(input("put a number:"))
e=eval(input("put a number:"))
i,e = min(i,e),max(i,e) 
clk=0
total=0
print(i,"到",e,"的非質數有:",end="")
for k in  range(i,e+1):
    if clk==0 and i==1:
        print("1",end=" ")
        clk=clk+1
        total=total+1
    else:
        for x in range(2,k+1):
            if k%x ==0 and x!=k:
                print(k,end=" ")
                total=total+k
                break
            elif k%x ==0 and x==k:
                break
print("\n總合為:",total)
