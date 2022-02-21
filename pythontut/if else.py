"""If Else"""
var1= int(input())
var2= int(input())
if var1>var2:
    print("Greater")
elif var1==var2:
    print("Equal")
else:
    print("lesser")

    # in gives true or false
    list=[5,6,3]
    print(6 in list)
    if 6 in list:
        print("Yes it is")
        if 12 not in list:
            print("not in list")