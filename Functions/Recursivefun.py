def recfun(n):  #Fact       orial using recursion
    if n == 0 or n == 1:
        return 1
    else:
        return n * recfun(n - 1)
    

res = recfun(5)
print(res)
