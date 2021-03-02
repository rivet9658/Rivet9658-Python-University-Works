#二數最大公因數
a=eval(input())
b=eval(input())
a,b=max(a,b),min(a,b)
r=a % b
while r !=0:
    a=b
    b=r
    r=a % b
print(a,"和",b,"的最大公因數是",b)
