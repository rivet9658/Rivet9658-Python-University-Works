#練習5-例題5
def main():
    (x1,y1)=eval(input("put a distance"))
    (x2,y2)=eval(input("put a distance"))
    distance(x1,y1,x2,y2)
def distance(a1,a2,b1,b2):
    answer=((a2-b2)**2+abs(a1-b1)**2)**(1/2)
    print("the distance of((",a1,",",a2,")",",","(",b1,",",b2,"))=",answer)
main()
