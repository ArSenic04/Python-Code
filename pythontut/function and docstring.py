"""Functions and docstrings"""
"""a=4
b=9
c=sum((a,b)) # Built in function
print(c)"""


def function2121():
    print("Hello you are in function")


# function2121()
def average122(x, y):
    """This is the program to print the average of two numbers"""  # This is called doc string
    avg = (x + y) / 2
    print(avg)
    # return avg


average122(5, 7)
# print(average122(5, 7))
# print(v)
print(average122.__doc__)  # this is the way to call the doc string
