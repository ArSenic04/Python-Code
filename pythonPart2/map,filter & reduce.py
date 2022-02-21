num = ["3", "23", "12"]
# for i in range(len(num)):
#     num[i]=int(num[i])
"""This is one way to typecast in lis"""
num = list(map(int, num))
print(num[2])


def sq(a):
    return a * a


# k = [2, 4, 3, 5, 7, 12, 8]
# spuare = list(map(sq, k))
# print(spuare)
"""Or"""
k = [2, 4, 3, 5, 7, 12, 8]
spuare = list(map(lambda x: x * x, k))
print(spuare)
"""Lambda is predefined function """


def cube(a):
    return a * a * a


hel = [sq, cube]
for i in range(5):
    w = list(map(lambda j: j(i), hel))
    print(w)

"""Filter function"""

l = [3, 2, 54, 36, 89, 12]


def is_greater_5(n):
    return n > 5  # This will give output as true or false


gr_than_5 = list(filter(is_greater_5, l))
print(gr_than_5)
"""Reduce"""
from functools import reduce

list1 = [1, 2, 3, 4]
y = reduce(lambda x, y: x + y, list1)
print(y)
