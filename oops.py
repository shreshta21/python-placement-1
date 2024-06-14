class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print(f"my name is {self.name}")
        print(f"idnumber:{self.idnumber}")
        
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)
        
    def details(self):
        print(f"my name is {self.name}")
        print(f"idnumber:{self.idnumber}")
        print(f"post: {self.post}")
        
a=Employee('Rahul',886012,200000,"Intern")
a.display()
a.details()