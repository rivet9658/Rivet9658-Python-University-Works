#三數最小公倍數
u=eval(input("put a number:"))
x=eval(input("put a number:"))
h=eval(input("put a number:"))
great=0
lcm=0
if u>x and u>h:
    great=u
elif x>u and x>h:
    great=x
else:
    great=h
while(True):
    if((great % u == 0) and (great % x == 0) and (great % h == 0)):
        lcm = great
        break
    great = great + 1
print(u,"和",x,"和",h,"的最小公倍數是",great)
