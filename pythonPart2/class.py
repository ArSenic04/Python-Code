class Employee:
    pass
# pass means nothing to write now
shivam = Employee()
arsenic= Employee()
shivam.age=18
arsenic.age=19
shivam.pet="arsenic"
arsenic.pet="shivam"
shivam.food= "Pizza"
arsenic.food="Burger"
print(shivam,arsenic)
print(shivam.__dict__)
# __dict__ is used to show the class variables in dictionary
print(arsenic.__dict__)

