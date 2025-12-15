def my_func(*x): #Arbitrary Arguments by using '*'
    print(x)

my_func()

# def my_func1(x):
#     print(x)     #positional argument: 'x'
# my_func1()       #Gives Error anyway missed Parameter

def my_func2(*x): #Function will recieve tuple of arguments and we can access them by using indexing in Print Function 
   print("Name is :"+ x[2])

my_func2('A','B','C')

#Functions with Key word Arguments
def my_func3(c1,c2,c3):
    print("the youngest child is:"+c3)
my_func3(c1='abc',c2='def',c3= 'ghi') # These are the KEY = VALUE arguments i.e.Key word arguments

# default argumetns
def my_func4(c1 = 'INDIA'): # INDIA is default argument
    print("This is :"+c1)
my_func4() # It will take India as default argument
my_func4('BHARATH')

def my_func5(a1):
    b = a1*a1
    return b
c = my_func5(4)
print("The Value is::", c)


def greet(a,b):  #Positional only Arguments
    print(f"The full name is:{a} and {b}")
    # print("The full name is:{a} and {b}") know the difference
    # print(f"The full name is:{} and {}".format(a,b)) # Gives Error f-string should not be null
    print("The full name is::: {} and {}".format(a,b))
    print(f"The name of b is in Argument only: {b}")

greet("Venkat","Durga") #These are the Positional arguments Only

greet("Venkat", b = "Amma") #Both Positional and Key word arguments
greet( b = "I too", a = "ILU") # arg's are not be in order it will works because of Keyword arguments

greet("","avr") #must pass no.of arguments


