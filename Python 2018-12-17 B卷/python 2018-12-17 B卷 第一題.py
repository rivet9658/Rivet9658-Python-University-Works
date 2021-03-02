#python 2018-12-17 B卷 第一題
a=[]
up=0
c=0
t=0
while True:
    j=eval(input())
    if j!=-9999:
        a.append(j)
    else:
        break

for i in a:
    up=up+i
    c=c+1
adv=up/c

for k in a:
    t=t+((k-adv)**2)
t=t**0.5
print(adv)
print(t)
