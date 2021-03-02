#練習3-例題3
a,b=eval(input("輸入兩個數字，後者必須大於前者:"))
t=0
if a>b:
    print("數值錯誤，請重新輸入")
else:
    for s in range(a,b+1):
        if s%2==0:
            t=t+s
            s=s+1
print(t)  
