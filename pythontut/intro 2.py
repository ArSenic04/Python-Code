mystr = "Shivam Ardeshna"
print(mystr[5])
print(len(mystr))#  len is the lenght of string in this case 18
""""
        S  h  i  v  a  m
index   0  1  2  3  4  5
"""
print(mystr[0:3])#  here 0:3 show print 3 indexsis
print(mystr[1:3])#  print 2 indexsis (excluding 0th index)
print(mystr[0:18])
print(mystr[0:54])
# this is error
# print(mystr[54])
# to skip the character
print(mystr[0:5:2])
print(mystr[0:5:1])
print(mystr[0:5:3])
print(mystr[::])   #   standard is 0:full lenght:1
print(mystr[::3443])   #   now 0 index is always printed now 3443 index is checked which is not there in string therefore 0 index is printed
print(mystr[-4  : -1])

#  Functions
# True and False are part of Boolean algebra
print(mystr.isalpha()) # This will show False because there are space in string which is not included in isalpha
print(mystr.endswith("na")) # This will show True
print(mystr.count("a")) # This will show the number of asked character present in string
print(mystr.capitalize()) # This will make first letter Capital
print(mystr.find("Ar")) # This will show the index where this is present
"""
lower() and upper() will make the string in lower and upper case respectively
"""
print(mystr.replace("Shivam", "Arsenic"))