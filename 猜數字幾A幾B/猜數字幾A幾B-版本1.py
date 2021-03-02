#猜數字幾A幾B版本1
import random
ans=[]
t=0
while t<4:
    ran=random.randint(1,9)
    if ran not in ans:
        ans.append(ran)
        t=t+1
for p in ans:
    print(p,end="")
print("\n")
while True:
    num=int(input())
    n=[]
    A=0
    B=0
    if num>9999 or num<1000:
        print("請重新輸入")
        continue
    for i in range(4):
        n.append(num%10)
        num=num//10
    n.reverse()
    if n.count(n[0])>1 or n.count(n[1])>1 or n.count(n[2])>1 or n.count(n[3])>1:
        print("請重新輸入")
        continue
    for i in range(4):
        if ans[i]==n[i]:
            A=A+1
            continue
        for j in range(4):
            if ans[i]==n[j]:
                B=B+1
    print("A:",A,",","B:",B)
    if A==4:
        break
print("success")
