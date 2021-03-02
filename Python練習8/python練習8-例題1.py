#練習8-例題1
lst=[]
while True:
    str=input()
    if str !="end":
        lst=str.split(":")
        print("hour:",lst[0],",min:",lst[1],",second:",lst[2])
    else:
        break
