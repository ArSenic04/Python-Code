import random
# random is module which import to this file
import sys

print(sys.path)
# This will show that how we import file from our system
import extra

print(extra.a)
# I have crreated extra file in which i declared a=9 and i imported that
"""OR"""
from extra import a

print(a)
# This is not the convenient method to use
import extra
extra.printjoke("joke")
# we use . to access the other parameters of any function or file etc.



"""AFTER THIS PROGRAM ALL OTHER ARE IN pythonPart2"""
