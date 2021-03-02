#三數最大公因數
a=eval(input())
b=eval(input())
c=eval(input())

gcd=1
k=2
while k <= a and k <=b and k <= c:
    if a % k ==0 and b % k ==0 and c % k ==0:
        gcd=k
    k=k+1
print("gcd(%d, %d, %d) = %d"%(a,b,c,gcd))
