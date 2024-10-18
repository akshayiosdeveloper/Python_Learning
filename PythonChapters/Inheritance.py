class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a Child Class
class Student(Person):
      def __init__(self, fname, lname,year):
       super().__init__(fname,lname)
       self.graduationyear = year

obj = Student(
    "a","kumar",2024
)
obj.printname()
print(obj.graduationyear)