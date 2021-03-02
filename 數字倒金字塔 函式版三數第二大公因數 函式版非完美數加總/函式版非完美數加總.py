#函式版非完美數加總
def main():
    c=eval(input())
    d=eval(input())
    c,d = min(c,d),max(c,d) 
    prefect(c,d)
    t=prefect(c,d)
    print("總和為:",t)
    
def prefect(x,y):
    total=0
    for i in range(x,y+1):
        s=0
        for j in range(1,i):
            if i%j==0:
                s=s+j
        if s!=i:
            total=total+i
    return total

main()
