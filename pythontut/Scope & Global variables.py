"""Scope & Global variables"""
l = 10  # global variable


def fun(m):
    # l = 5
    n = 8
    global l
    l += 45
    print(l, n)
    print(m, "printed")


fun("This is me is")
print(l)
