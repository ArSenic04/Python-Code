"""List,tuple"""
grocery = ["Harpic" , "23" , "eraser"  , "eggs" , "thoothpaste" , "Pencil"]

print(grocery)
print(grocery[4])
numbers = [2,6,34,11,8,21]
# To sort the numbers we use sort()
"""numbers.sort()
print(numbers)"""
#  Append is used to add number at the last
numbers.append("Shivam" + "33")
print(numbers)
print(numbers[0:5:3])

# to reverse the numbers we use reverse()
"""numbers.reverse()
print(numbers)"""
# Mutable - can change
# immutable - cannot change ->> Tupple
tp=(1,4,7)
print(tp)
"""To reverse the number very easy"""
a=1
b=8
a,b = b,a
print(a,b)