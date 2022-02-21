"""Printing Pattern"""
print("Enter any interger")
n = int(input())
bool_val = int(input("1 for true and 0 for false"))
if bool_val == 1:
    for k in range(0, n + 1):
        print("*" * k)
        n = n - 1

else:
    for i in range(n,0,-1):
        print("*"*i)
        n=n-1
