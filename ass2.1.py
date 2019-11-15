sub1 = int(input("English Marks = "))
sub2 = int(input("Python Marks = "))
sub3 = int(input("Networking Marks = "))
sub4 = int(input("Physics Marks = "))
sub5 = int(input("Calculus Marks = "))
per = ((sub1 + sub2 + sub3 + sub4 + sub5)/500)*100
if (per<100 and per>=90):
    print("Grade is A1")
elif (per<=89 and per>=80):
    print("Grade is A")
elif (per<=79 and per>=70):
    print("Grade is B")
elif (per<=69 and per>=60):
    print("Grade is C")
elif (per<59):
    print("Grade is F")