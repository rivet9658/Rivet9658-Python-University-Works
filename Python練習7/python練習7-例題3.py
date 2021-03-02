#練習7-例題3
def inputdata(setc):
    while True:
        a=eval(input())
        if a!=-9999:
            setc.add(a)
        else:
            break
    return setc

def operation(set11,set12):
    print()
    print("set1|set2=",set11|set12)
    print("set1&set2=",set11&set12)
    print("set1-set2=",set11-set12)
    print("set1^set2=",set11^set12)
    print("set1 is a subset of set2:",set11.issubset(set12))
    print("set1 is a superset of set2:",set11.issuperset(set12))
    
def main():
    print("input set1 data:")
    set1=set()
    inputdata(set1)
    
    print("input set2 data:")
    set2=set()
    inputdata(set2)
    
    print("set1:",set1)
    print("set2:",set2)
    operation(set1,set2)
    
main()
