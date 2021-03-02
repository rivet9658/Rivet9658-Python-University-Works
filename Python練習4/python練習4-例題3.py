#練習4-例題3
num1 = eval(input("put a number"))
num2 = eval(input("put a number"))
num1,num2=min(num1,num2),max(num1,num2)
test=2
for i in range(num1,num2+1):
    for j in range(test,i+1):
        if i%j==0 and j!=i:
            break
        elif i%j ==0 and j==i:
            print(i,end=" ")
            break
