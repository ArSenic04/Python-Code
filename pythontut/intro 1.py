v1 = "my name is shivam"
v2 = 3
v3 = 36.12
v4 = "nickname ArSenic"
v5 = "34"
v6 = "30"
print("Hello world")
print(type(v1))
print(type(v2))
print(type(v3))
print(v2+v3)
print(v1 + v4)
print(v5 + v6)
# comment for Python
"""This is multiline
comment"""
# Typecasting
print(int(v5) + int(v6))
print(5*v1)
# or
print(5*"My name is shivam\t")
print(5*"My name is shivam\n")
"""
str()
float()
int()
"""
print(10*int(v5) + int(v6))  # 10*34 + 30
print(10*str(int(v5) + int(v6)))
# Taking the values from the user
print("Enter the number")
hi = input()  # input is as string
# hi is any variable
print("Your number is",hi)
print("Your number after adding 10 is",int(hi)+10)
