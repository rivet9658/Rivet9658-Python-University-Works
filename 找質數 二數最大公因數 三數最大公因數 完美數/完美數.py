#完美數
c=eval(input())
d=eval(input())
c,d = min(c,d),max(c,d) 
total = 0
answer = []
for i in range(c,d+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s==i:
        answer.append(i)
        total=total+i
print(c,"到",d,"之間的完美數有:")
for p in answer:
    print(p,end=" ")
print("\n總和為:",total)
