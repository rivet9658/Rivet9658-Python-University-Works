#階梯排列(右上到左下,大到小)
c=eval(input("輸入一個<20的正整數:"))
h=0
if c>20 or c<=-1:
    print(c,"非範圍值，請重新輸入")
else:
    for k in range(0,c+1):
        for j in range(k,0,-1):
            while h<c-k:
                print("    ",end="")
                h=h+1
            print("%4d" % (j),end="")
            if j==1:
                print("\n")
                h=0
