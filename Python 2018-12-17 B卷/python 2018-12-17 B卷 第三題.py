#python 2018-12-17 B卷 第三題
x=[]
check=2
a=0
b=0
ip1=eval(input())
for i in range(0,ip1):
    ip2=eval(input())
    x.append(ip2)
min1=min(x)
le=len(x)
x.sort()

while check<=min1:
    for k in x:
        if k % check==0:
            a+=1
        else:
            a=0
    if a==le:
        b=check
    else:
        a=0
    check+=1
if b!=0:
    print("最大公因為:",b)
else:
    print(0)
