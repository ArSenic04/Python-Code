def factorial(n):
    fac = 1
    for i in range(0, n):
        fac = fac * i
    return fac


n = int(input("Enter the number"))
a = factorial(n)
print(a)
