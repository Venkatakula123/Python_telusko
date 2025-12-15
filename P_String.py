#String Operations in Python
str = "Hello World"
str = "Hello"

print(type(str))

str1 = "Hello"
str2 = 'World'
str3 = '''Hello World str3'''
print(str1)
print(str2) 
print(str3)

str4 = """Hello World str4"""
print(str4)

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
#print(str[5])

print("String Lengthis ==",len(str))
print(str[0:5])
print(str[0:6])
print(str[0:7])

print(str[:])#Hello
print(str[2:5])#ll0
print(str[2:7])#llo
print(str[:5])#Hello
print(str[:-1])#Hell

print(str[:-2])#Hel

#Reverse String
print(str[::-1])

print('Hello'+'Apple')
print('Hello'+' '+'Apple')

print('o' in str)

print('o' not in str)