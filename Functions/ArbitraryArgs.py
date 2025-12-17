def arbfun(*args):
    for i in args:
        print(i)

arbfun(1,2,3,4,5,6,7,8,9,10) #it will print the argumants one by one instead of printing in tupls

# Now we can able to print the arbitrary arguments as a tuple
def arbfun2(*args):
    print("The arbitrary arguments as tuple is :", args)
    print(f"The type of args is : {type(args)}")
    print(f"The first element in args is : {args[0]} ")
    print(f"The last element in args is : {args} type of last element is {type(args)} ")

#arbfun2(1,2,3,4,5,6,7,8,9,10)

#Passing the List as a arbitrary arguments
list1 = [11,22,33,44,55,66,77,88,99,110]
arbfun2(*list1)  #unpacking the list while passing as arbitrary arguments
