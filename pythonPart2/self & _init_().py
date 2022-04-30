class shree:
    pass
    def __init__(self,aage,apet,afood):
        self.age=aage
        self.pet=apet
        self.food=afood

    def printdetails(self):
        print(f"{self.age} {self.pet} {self.food}")

"""This is for init function"""
shivam = shree(18,"arsenic","Pizza")
print(shivam.food)
"""This is for self used in printdetails function"""
arsenic = shree()
shivam.age=18
arsenic.age=19
shivam.pet="arsenic"
arsenic.pet="shivam"
shivam.food= "Pizza"
arsenic.food="Burger"
arsenic.printdetails()