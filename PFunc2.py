def calculate(a, b):    
    """This function returns the sum and difference of two numbers."""    
    return a + b, a - b    
# Calling the function and unpacking the result    
sum_result, diff_result = calculate(10, 4)    
print(f"Sum: {sum_result}, Difference: {diff_result}")    

#https://www.tpointtech.com/def-function-in-python
def phello():
    print("Hello world")

phello()

def parg(name):
    """This function greets the user by name."""   
    print(f"the name is {name}")

parg("Avr")

# Using the default argument in functions
def dargs(name = "Venkat"):
    print(f"Calling {name}")

dargs()
dargs("Durga")

#Keyword arguments
def kargs(a,b):
    print("The {} and {}".format(a,b))

kargs(a='abc',b='def')

#Arbitrary Arguments
def aargs(*names):
    for n in names:
        print(f"The names are {names}") #It will prints tuple every time
        print(f"The names are {n}") #It will prints a element for every time 

aargs("a","bc","ef","gh")