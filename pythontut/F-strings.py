"""F- Strings"""
l = "shivam"
# this is the way to replace the formate specifiers with another in Python
k = "This is %s"
print(k % l)
print("Enter the score")
m = "virat Kohli scored %d runs in t20"
v = int(input())
print(m % v)
# print("But Still He is out from Cricket team in T20 in 2021")
"""Format function"""
h="there was {} {}"
a="dog"
b="cat"
op=h.format(a,b)
# {} {} bracket in h will be replace by a and b
print(op)