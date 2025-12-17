def argus(a,b=10,*args,**kwargs):
    print("a is:",a)
    print("b is ",b)
    print("*args are :", args )
    print("**kwargs are:", kwargs)

argus(1,2,3,4,5,6,7,8, x=10, y=20,z=30)

kwargs = {'x' : 10,'y' : 20}
#print(f"kwargs {kwargs} ")

args = ('a','b','c','d')
#print(f"{args}")


a = 1
#print(argus(a)) #it works and b will take default value 10 *args and **kwargs will be empty

print(argus()) # it will give error as a is mandatory positional argument

