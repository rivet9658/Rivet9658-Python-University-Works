#練習8-例題2
string=input()
l=len(string)
s1=string[0]
s2=string[1:l]
if s1.isalpha()==True:
    if s2.isalnum()==True:
        print("合法變數名稱")
    else:
        print("不合法變數名稱")
else:
    print("不合法變數名稱")
