#練習2-例題3
import random
a=random.randint(1,100)
if a%3==0:
    if a%5==0:
        print(a,"既是3也是5的倍數")
    else:
        print(a,"是3的倍數")
elif a%5==0:
    if a%3==0:
        print(a,"既是3也是5的倍數")
    else:
        print(a,"是5的倍數")
else:
    print(a,"不是3也不是5的倍數")

