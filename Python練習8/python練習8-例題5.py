#練習8-例題5
while True:
    s1=input()
    l=len(s1)
    if l<20:
        print("請重新輸入，請至少輸入20個字")
    else:
        for i in range(0,l):
            if s1[i].isupper()==True:
                print(s1[i],":is a upper alpha")
            elif s1[i].islower()==True:
                print(s1[i],":is a lower alpha")
            elif s1[i].isdigit()==True:
                print(s1[i],":is a number")
            elif s1[i]==" ":
                print(s1[i],":is a space")
            else:
                print(s1[i],":is other")
        break
