"""*args and **kargs"""


def funarg(nor, *args, **kwargs):
    print(nor)
    for i in args:
        print(i)
    print(type(args))  # Tuple
    for k, l in kwargs.items():
        print(f"{k} likes {l}")


nor = "Hello Guys"
hi = ["Shivam", "hello", "hero"]
kw = {"Shivam": "coding", "harry": "pizza", "ronil": "coca cola"}
funarg(nor, *hi, **kw)
