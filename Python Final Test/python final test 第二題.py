#python final test 第二題
stun=[]
stuh=[]
stuw=[]
bmi=[]
n=eval(input())

def main(stun,stuh,stuw,bmi,n):
    math(stun,stuh,stuw,bmi,n)
    check(stun,stuh,stuw,bmi,n)
    
def math(stun,stuh,stuw,bmi,n):
    for i in range (0,n):
        print("請輸入姓名:")
        stun.append(input())
        print("請輸入身高(cm):")
        stuh.append(eval(input()))
        print("請輸入體重(kg):")
        stuw.append(eval(input()))
        bm=int(stuw[i])/((int(stuh[i])/100)**2)
        bmi.append(bm)
    return(stun,stuh,stuw,bmi,n)

def check(stun,stuh,stuw,bmi,n):
    print("輸入搜索姓名:")
    ch=input()
    s=0
    for i in range(0,n):
        if ch == stun[i]:
                print("姓名:",stun[i],"身高:",stuh[i],"體重:",stuw[i],"BMI:",bmi[i])
        else:
             s=s+1
    if s==n:
        print("not found")
main(stun,stuh,stuw,bmi,n)
