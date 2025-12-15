x = [1, 2, [3, 4, 5], 6, 7] 
# this is nested list
print (x[2])
# Output: [3, 4, 5]
print (x[2][1])

print("====================================")

x=y=[7,8,9]
print(y)
print(x[0])

print("====================================")

a,b,c = 1,2,3
print(type(a))

print("====================================")
a = 1,2,3
print(type(a))

print("====================================")
#a, b, _ = 1,2,3,4

#print("====================================")
#a,b = 1,2,3
#print(a,b)

#print("====================================")
#a, b, c = 1, 2
#print(a, b, c)

print("====================================")
a = b = c = 1 # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1
b = 2 # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1 # so output is as expected.

print("====================================")
x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7,8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
print(y) # printing the value of the list using its other name
# Output: [13, 8, 9] # hence, naturally the change is reflected

print("====================================")
x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
print(x[2])
# Output: [3, 4, 5]
print(x[2][1])
# Output: 4

