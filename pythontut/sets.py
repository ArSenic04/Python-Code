"""Set"""
s=set([1,5,3,9])
print(s)
"""Set only contain unique numbers"""
s.add(2)
s1=s.union({1,4,6})
s2=s.intersection({2,7,3})
print(s,s1,s2)