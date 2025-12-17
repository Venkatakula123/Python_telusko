def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

# Using keyword arguments
greet(age=25, name="Venkat")

#f-string: More concise and readable, directly embeds variables in the string.

#This uses an f-string (formatted string literal), which allows you to embed expressions inside curly braces {} directly within the string.
#It results in a clean and readable output, where the values of name and age are directly inserted into the string.