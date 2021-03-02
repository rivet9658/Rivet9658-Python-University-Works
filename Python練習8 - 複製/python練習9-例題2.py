#練習9-例題2
outfile=open("score.txt","w")
while True:
    name=input()
    score=input()
    if name=="none":
        break
    else:
        outfile.write(name)
        outfile.write("\n")
        outfile.write(score)
        outfile.write("\n")
