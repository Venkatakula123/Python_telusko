x = None # None Data type it's like null in Some other Programming Languages
print(x)
print(type(x))

def my_fun():
    pass

result = my_fun()
print(result)

if x is None:
    print("x is None")

# Numeric Data Types 
''' INT, FLOAT, COMPLEX, BOOLEAN'''

num = 2.5
print(type(num))

num = 5
print(type(num))

num = 5+6j
print(type(num))

a = 5.6
print(a)

b = int(a)
print(b)


k = float(b)
print(k)

k = 6
c = complex(b,k)
print(c)


bool = b < k
print(bool)
print(type(bool))

a = int(True)
print(a)

b = int(False)
print(b)

lst = [1,2,3,4,5]
print(type(lst))

s = {1,2,3,4,'f','g'}
print(type(s))

name = 'VenkateswarReddy'
print(type(name))
# There is no char data type in Python
#range
ar = range(10)
print(ar)
print(list(ar))

print(set(ar))

print(tuple(ar))

b = range(2,20,2)
print(list(b))

d = {'a':1,'b':2,'c':3,'d':4}
print(d.keys())
print(d.values())

print(d['a'])
print(d.get('c'))

print(6/3) # gives coeficient
print(4%2) #gives reminder