#練習6-例題5
lst35=[]

def main(lst35):
    inputData(lst35)
    total(lst35)

def inputData(lst):
    for i in range(0,3):
        lst.append([])
        print("#%d student"%(i+1))
        for j in range(0,5):
            score=eval(input())
            lst[i].append(score)
    return lst

def total(lst2):
    a=0
    for i in range(0,3):
        for j in range(0,5):
            a+=lst2[i][j]
        print("#%d student"%(i+1))
        print("sum = ",a,", ","average = ",a/5)
        a=0
    
main(lst35)
