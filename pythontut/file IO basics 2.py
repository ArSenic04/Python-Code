# f= open("shivam.txt","a")
# a=f.write("Shivam is very nice\n")
# print(a)
# f.close()

# f= open("shivam.txt","w")
# a=f.write("Shivam is very nice\n")
# print(a)
# f.close()

# f=open("shivam.txt", "r+")
# print(f.read())
# f.write("Thank you")

""" seek() and tell()"""
f= open("shivam.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(0)
print(f.readline())
# print(f.tell())

f.close()
