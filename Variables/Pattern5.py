n = 5
for i in range(1, n + 1):
    for j in range(n - 1, i-1, -1):
        print(" ", end="")
        #print(list(range(n - 1, i-1, -1)))
    for k in range(1, i + 1):
        print("*", end="")
    print()


for i in range(1,6):
    print(i)