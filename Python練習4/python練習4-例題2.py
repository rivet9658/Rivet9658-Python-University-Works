#練習4-例題2
num1 = eval(input("put a number"))
num2 = eval(input("put a number"))
ans=[]
test=2
while True:
    if num1&test==0 and num%test==0:
        ans.append(test)
        break
    else:
        test=test+1
print(max(ans))
