class Employee:
    pass
    def printdetails(self):
        return f"Name is {self.name} age is {self.age} role is {self.role}"

shivam = Employee()
arsenic = Employee()
shivam.name = "Shivam"
arsenic.name = "Arsenic"
shivam.age= "18"
arsenic.age ="19"
shivam.role = "Devloper"
arsenic.role = "a second person"
print(arsenic.printdetails())