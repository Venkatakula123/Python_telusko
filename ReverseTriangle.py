n = int(input("Enter the Number"))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end = "")
    print()