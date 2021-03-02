#函式版三數第二大公因數
def main():
    a=eval(input())
    b=eval(input())
    c=eval(input())
    factor(a,b,c)
    answer=factor(a,b,c)
    print(answer)
    
def factor(x,y,z):
    gcd=0
    k=2
    get=0
    check=0
    while k <= x and k <= y and k <= z:
        if x % k ==0 and y % k ==0 and z % k ==0:
                check=k
        k=k+1
    k=2
    while k <= x and k <= y and k <= z:
        if x % k ==0 and y % k ==0 and z % k ==0:
            if k == check:
                break
            else:
                gcd=k
        k=k+1
    return gcd
main()
