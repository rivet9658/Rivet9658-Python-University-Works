#練習9-例題3
infile=open("friends.txt","r")
for i in range(1,6):
    info=infile.readline()
    print(info)
infile.close()
