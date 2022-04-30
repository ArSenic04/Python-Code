"""List Comprehensions"""
ls = [i for i in range(14) if i % 3 == 0]
print(ls)
"""Dictionary Comprehensions"""
dict = {i: f"iteam{i}" for i in range(12)}
print(dict)
d={value:key for key,value in dict.items()}
print(d)
