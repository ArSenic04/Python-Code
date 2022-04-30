# iterable- __iter__() or __getitem__()
# iterator- __next()__
def gen(n):
    for i in range(n):
        yield i
        # yield is a generator
        """ generator is storing the things to make process ready and it will store that function at some 
        address to save memory"""
k=gen(5)
print(k)
print(k.__next__())# next will print the one number at time that's why it is iterator
s="shivam"
m=iter(s)
print(m.__next__())
print(m.__next__())

