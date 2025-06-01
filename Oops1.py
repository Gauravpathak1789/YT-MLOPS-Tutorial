# Initiate a class
class Employee:
    #special method to initialize the class
    def __init__(self):
        print("started executing attributes")
        self.id=123
        self.salary=50000
        self.designation="Software Engineer"
        print("Attributes initialized")

    def travel(self,destination):
        print("Employee is now travelling to", destination)
# create object of the class
obj=Employee()
# print("Employee ID:", obj.id)
# print(obj.travel("Banaras"))