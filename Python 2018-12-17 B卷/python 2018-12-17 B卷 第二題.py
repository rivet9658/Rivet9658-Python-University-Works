#python 2018-12-17 B卷 第二題
ip1=eval(input())
ip2=eval(input())
ip1,ip2=min(ip1,ip2),max(ip1,ip2)
answer=[]
total=0
for i in range(ip1,ip2+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s==i:
        answer.append(i)

for k in answer:
    print(k,end=" ")
    total+=k
print("\n")
print(total)
