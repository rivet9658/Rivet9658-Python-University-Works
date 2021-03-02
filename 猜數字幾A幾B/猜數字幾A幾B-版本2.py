#猜數字幾A幾B版本2
import random
ans=[]
t=0
while t<4:
    ran=str(random.randint(1,9))
    if ran not in ans:
        ans.append(ran)
        t=t+1

for p in ans:
    print(p,end="")
print("\n")

while True:
    num=list(input())
    A=0
    B=0
    if len(num)!=4:
        print("請重新輸入")
        continue
    if num.count(num[0])>1 or num.count(num[1])>1 or num.count(num[2])>1 or num.count(num[3])>1:
        print("請重新輸入")
        continue
    for i in range(4):
        if ans[i]==num[i]:
            A=A+1
            continue
        for j in range(4):
            if ans[i]==num[j]:
                B=B+1
    print("A:",A,",","B:",B)
    if A==4:
        break
print("success")
