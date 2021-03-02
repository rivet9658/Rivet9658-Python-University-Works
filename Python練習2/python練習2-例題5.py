#練習2-例題5
h=eval(input('input a number='))
if h%5==0:
    if h%8==0:
      print(h,"can be diviended by 5 and 8")
    else:
      print(h,"can be diviended by 5")
elif h%8==0:
    if h%5==0:
      print(h,"can be diviended by 5 and 8")
    else:
      print(h,"can be diviended by 8")
else:
 print(h,"can't be diviended by 5 or 8")
