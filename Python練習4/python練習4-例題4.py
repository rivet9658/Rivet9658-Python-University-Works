#練習4-例題4
a=0
b=0
c=0
invalid=0
choice=0
for i in range(0,11):
    print("1:Peter")
    print("2:Nancy")
    print("3:Mary")
    choice=eval(input("Which one do you prefer:"))
    print("\n")
    if choice == 1:
        a=a+1
    elif choice == 2:
        b=b+1
    elif choice == 3:
        c=c+1
    else:
        invalid=invalid+1
print("Peter:",a,"Nancy:",b,"Mary:",c)
print("invalid:",invalid)
