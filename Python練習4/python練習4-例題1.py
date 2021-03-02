#練習4-例題1
num = eval(input("put a number"))
test=2
while True:
    if num%test==0:
        print(test)
        break
    else:
        test=test+1
