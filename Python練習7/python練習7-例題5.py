#練習7-例題5
dict10={}
while True:
    print("1:add")
    print("2:delete")
    print("3:query")
    print("4:display")
    print("5:exit")
    print("Which one:",end="")
    ch=eval(input())
    if ch ==1:
        print("input key:",end="")
        k=eval(input())
        print("input value:",end="")
        v=eval("input()")
        dict10[k]=v
    elif ch==2:
        print("input key:",end="")
        delete=eval(input())
        if delete in dict10:
            del dict10[delete]
            print(delete,"has been delete")
        else:
            print("not found the key")
    elif ch==3:
        print("input key:",end="")
        found=eval(input())
        if found in dict10:
            print(dict10[found])
        else:
            print("not found the key")
    elif ch==4:
        print(dict10)
    elif ch==5:
        break
    else:
        print("it is a error number")
