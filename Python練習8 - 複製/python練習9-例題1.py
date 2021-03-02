#練習9-例題1
outfile=open("friends.txt","w")
for i in range(1,6):
    data=input()
    outfile.write(data)
    outfile.write("\n")

outfile.close()
