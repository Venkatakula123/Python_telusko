marks = int(input("Enter your Marks to know the grade"))

if marks > 90:
    print("A grade")
elif marks > 80:
    print("B grade")
elif marks > 70:
    print("C grade")
elif marks > 60:
    print("D grade")
elif marks > 40:
    print("E grade")
else:
    print("Failed")