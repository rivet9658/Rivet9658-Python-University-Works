#練習5-例題2
def gpa(grade):
    if grade>=90 and grade <=100:
        print("Your gpa is A")
    elif grade>=80 and grade <=89:
        print("Your gpa is B")
    elif grade>=70 and grade <=79:
        print("Your gpa is C")
    elif grade>=60 and grade <=69:
        print("Your gpa is D")
    elif grade<=59:
        print("Your gpa is E")
    else:
        print("Your grade is not true")
def main():
    x=eval(input("puy your grade:"))
    gpa(x)
main()
