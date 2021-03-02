#階梯排列(由右上到左下,小到大)
c=eval(input("輸入一個<100的正整數:"))
h=0
if c>=100 or c<=-1:
    print(c,"非範圍值，請重新輸入")
else:
    for k in range(0,c+1):
        for j in range(0,k):
            while h<c-k:
                print("    ",end="")
                h=h+1
            print("%4d" % (j+1),end="")
            if j==k-1:
                print("\n")
                h=0
