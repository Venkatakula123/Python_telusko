def nestfun(**kargs):
    print(kargs)
    nfun(**kargs)
def nfun(**kargs):
    print("Inside nested function")
    print(len(kargs))

nestfun( a =1, b  =2, c =3, d =4, e =5) #Calling the main function which in turn calls the nested function

nfun(a=1, b=2, c=3, d=4, e=5) #Directly calling the nested function without calling the main function