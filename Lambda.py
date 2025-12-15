n = lambda x : x + 10  
  
#printing the output, and 10 is the value of x   
print(n(10))

n = lambda x: "Zero" if x == 0 else "Even" if x % 2 == 0 else "Odd"  
print(n(0))

n = [lambda a = x: 
     a * 10 
     for x in range(1, 6)]  
for i in n:
    print(i())