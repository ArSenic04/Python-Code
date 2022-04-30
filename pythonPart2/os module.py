import os

# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
"""How to remove the directories"""
directory = "a"

# Parent Directories
parent_dir = "C:/Users/a_moh/PycharmProjects/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'Nikhil'
# os.makedirs(path)
# print("Directory '% s' created" % directory)
os.rmdir(path)

"""How to add new directories"""

directory = "a"

# Parent Directories
parent_dir = "C:/Users/a_moh/PycharmProjects/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'Nikhil'
# os.makedirs(path)
# print("Directory '% s' created" % directory)
os.mkdir(path)

"""How to list down number of files or directories"""
path = "C:/Users/a_moh/PycharmProjects"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)
