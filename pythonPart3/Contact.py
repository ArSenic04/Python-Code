from collections import OrderedDict


class contact:
    def display(self, name, number):
        for i, j in contactlist.items():
            print(i, ":", j)


c = contact()
contactlist = {}
while (True):
    print("1.Display the contact list")
    print("2.Add the number")
    use = int(input())
    if use == 1:
        c.display(c.name, c.number)
    elif use == 2:

        print("Enter The number ")
        c.number = int(input())
        print("Enter the name of that Person")
        c.name = input()
        if c.number in contactlist.values():
            print(f"This Number is of {c.name}")
            continue

        print("This Number is updated to contact list")
        contactlist.update({c.name: c.number})
        print(contactlist)
    else:
        print("Invalid Input")

    print("Press q to Quit and c To Continue")
    user_choice2 = ""
    while (user_choice2 != "c" and user_choice2 != "q"):
        user_choice2 = input()
        if user_choice2 == 'q':
            exit()
        elif user_choice2 == 'c':
            continue
        else:
            print("Not a valid Option")
