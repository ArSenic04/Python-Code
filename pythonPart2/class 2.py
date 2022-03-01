class Employee:
    no_of_leaves = 8
    pass

    def printdetails(self):
        return f"Name is {self.name} age is {self.age} role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


shivam = Employee()
arsenic = Employee()
shivam.name = "Shivam"
arsenic.name = "Arsenic"
shivam.age = "18"
arsenic.age = "19"
shivam.role = "Devloper"
arsenic.role = "a second person"

print(arsenic.printdetails())
shivam.change_leaves(34)
print(shivam.no_of_leaves)
