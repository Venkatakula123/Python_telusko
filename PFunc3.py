def my_decorator(func):    
    """This is a simple decorator."""    
    def wrapper():  
        func()  
        print("Something is happening before the function is called.")    
            
        print("Something is happening after the function is called.")
        func()    
    return wrapper    
@my_decorator    
def say_hello():    
    print("Hello!")    
# Calling the decorated function    
say_hello()    