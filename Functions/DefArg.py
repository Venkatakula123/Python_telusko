def funLoop(x = 6):
    for i in range(1,x):
        if i % 2 == 0:
            print("Even",i)
        else:
            print("Odd",i) 

x1 = int(input("Enter some number to print Evevn's::"))
#res = funLoop(x1)

print(funLoop(x1))