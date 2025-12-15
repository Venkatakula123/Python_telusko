def my_function(*x):
    return x * 2
print(my_function(2,4,5,6))

# Explanation:

# def my_function(*x):
# This defines a function that takes a variable number of arguments. The *x collects all arguments into a tuple named x.

# return x * 2
# This tries to multiply the tuple x by 2. In Python, multiplying a tuple by an integer repeats the tuple, so (2, 4, 5, 6) * 2 results in (2, 4, 5, 6, 2, 4, 5, 6).

# print(my_function(2,4,5,6))
# This calls the function with four arguments and prints the result, which will be (2, 4, 5, 6, 2, 4, 5, 6).