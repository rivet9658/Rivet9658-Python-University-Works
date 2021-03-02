#練習7-例題4
dict10={}

while True:
    print("input key:",end="")
    k=eval(input())
    print("input value:",end="")
    v=eval("input()")
    if k !=-9999:
        dict10[k]=v
    else:
        break
        
print(dict10)
print("what key do you wnat to delete:",end='')
found=eval(input())

if found in dict10:
    del dict10[found]
    print(dict10)
else:
    print("not found")
