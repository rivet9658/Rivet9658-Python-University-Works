#練習7-例題1
import random
number=[]
for i in range(0,10):
    number.append(random.randint(1,100))
tuple1=tuple(number)
print(number)
print(tuple1)
