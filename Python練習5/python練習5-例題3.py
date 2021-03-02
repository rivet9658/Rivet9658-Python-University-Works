#練習5-例題3
def BMI(high,weight):
    bmi=weight/((high/100)**2)
    if bmi < 18.5:
        print("Your bmi is under weight")
    elif bmi >= 18.5 and bmi <25:
        print("Your bmi is normal")
    elif bmi >= 25 and bmi <30:
        print("Your bmi is over weight")
    elif bmi >= 30:
        print("Your bmi is fat")
def main():
    x=eval(input("put your high"))
    y=eval(input("put your weight"))
    BMI(x,y)
main()
