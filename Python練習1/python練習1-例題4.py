#練習1-例題4:
m=eval(input("輸入熱水量:"))
initialT=eval(input("輸入起始溫度:"))
finalT=eval(input("輸入最終溫度:"))
q=m*(finalT-initialT)*4184
print("所需能量:",q)
