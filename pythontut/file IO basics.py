"""File  IO BASICS"""
"""
r -> open file for reading mode - default
w -> open file for writing
x -> create file if not exists
a -> add more content to file
t -> text mode - default
b -> binary mode
+ ->  read and write
"""
f = open("shivam.txt","r")
hi = f.read(4)
# print(hi)
# f.close()
for line in hi:
    print(line)