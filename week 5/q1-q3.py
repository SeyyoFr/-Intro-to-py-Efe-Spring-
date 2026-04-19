class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self. birtdate = ""
        self. phone_number = ""
    
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

p1 = Person("Efe Seyit ", "Uçak ")
p1.set_birthdate("07/09/2005")
p1.set_phone_number("+420 777-749-063")

print(p1.firstname)
print(p1.lastname)
print(p1.birthdate)
print(p1.phone_number)

class Employee(Person):
    def __init__(self, firstname, lastname, company, salary):
        super().__init__(firstname, lastname)
        self.company = company
        self.salary = salary

e1 = Employee("Efe Seyit", "Uçak", "Suny", 100000)
e1.set_birthdate("07/09/2005")
e1.set_phone_number("+420 777-749-063")

print(e1.firstname)
print(e1.lastname)      
print(e1.birthdate) 
print(e1.phone_number)  
print(e1.company)   
print(e1.salary)    
