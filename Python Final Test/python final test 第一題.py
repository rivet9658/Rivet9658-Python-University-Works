#python final test 第一題
lst=[]
while True:
    str=input()
    if str !="end":
        lst=str.split(":")
        if int(lst[0])>24:
            print("請輸入正確的時間")
        else:
            if int(lst[0])>=13:
                k=int(lst[0])-12
                print("下午",k,"點",lst[1],"分",lst[2],"秒")
                k=0
            else:    
                print("上午",lst[0],"點",lst[1],"分",lst[2],"秒")
    else:
        break
