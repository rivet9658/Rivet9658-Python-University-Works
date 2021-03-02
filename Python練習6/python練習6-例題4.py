#練習6-例題4
alst=[]

def main(alst):
    for i in range(0,10):
        alst.append(eval(input()))
    print(alst)  
    mm,ss=meanAndsd(alst)
    print()
    print(mm,ss)

def meanAndsd(lst):
    mean=0
    sta=0
    for j in range(0,10):
        mean+=lst[j]
    mean=mean/10
    for k in range(0,10):
        sta+=(lst[k]-mean)**2
    sta=(sta/10)**0.5
    return mean,sta

main(alst)
