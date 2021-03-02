#二數最小公倍數
u=eval(input("put a number:"))
x=eval(input("put a number:"))
great=0
lcm=0
if u>x:
    great=u
else:
    great=x
while(True):
    if((great % u == 0) and (great % x == 0)):
        lcm = great
        break
    great = great + 1
print(u,"和",x,"的最小公倍數是",great)
