#練習5-例題1
def multiply99():
    a=1
    b=1
    while True:
        print(a,"*",b,"=",a*b,end=" ")
        if a<9:
            a=a+1
        else:
            print("\n")
            a=1
            if b<9:
                b=b+1
            else:
                break              
multiply99()
