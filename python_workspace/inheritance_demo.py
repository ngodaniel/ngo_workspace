#a python program to demonstrate inheritance

#base or super class. note object in bracket.
#(generally, object is made ancestor o fall classes)

class Person(object):
    #constructur
    def __init__(self,name):
        self.name=name
        
    #to get name
    def getName(self):
        return self.name

    #to check if this person is employee
    def isEmployee(self):
        return False

#inherited or sub class (note person in bracket)
class Employee(Person):
    #here we return true
    def isEmployee(self):
        return True


emp=Person("Geek1") #an object of person
print(emp.getName(),emp.isEmployee())

emp=Employee("Geek2") #an object of employee
print(emp.getName(),emp.isEmployee())