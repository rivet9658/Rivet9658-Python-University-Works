#練習8-例題4
lst=[]
while True:
    s1=input()
    if s1 !="end":
        if s1.endswith("e")==True:
            lst.append(s1)
    else:
        break
print(lst)
