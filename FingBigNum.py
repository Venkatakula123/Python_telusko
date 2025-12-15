#Find the biggest number from 4 no's

a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
d = int(input("Enter d"))
"""
if a>b:
    if a>c:
        if a>d:
            print("a is biggest")
        else:
            print("d is biggest")
    elif c>d:
        print("c is biggest")    
    else:    
        print("d is biggest")
elif b>c:
    if b>d:
        print("b is biggest")
    else:
        print("d is biggest")
elif c>d:
    print("c is biggest")
else:
    print("d is biggest")
"""
if a>b and a>c and a>d:
    print("a is biggest")
elif b>c and b>d:
    print("b is biggest")
elif c>d:        
    print("c is biggest")
else:
    print("d is biggest")