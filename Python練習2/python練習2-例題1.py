#練習2-例題1
a,b,c=eval(input('input 3 number='))
d=(b**2)-(4*a*c)
if d>0:
 print('此方程式有相異2個解')
 answer1=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
 answer2=(-b-((b**2)-(4*a*c))**0.5)/(2*a)
 print(answer1,answer2)
elif d==0:
 print('此方程式有相同2個解')
 answer1=(-b+((b**2)-(4*a*c))**0.5)/(2*a)
 print(answer1)
else:
 print('此方程式無解')

