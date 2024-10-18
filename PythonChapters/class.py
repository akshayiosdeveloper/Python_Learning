class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

# The __init__() Function
class Person:
    def __init__(self,name,age) :
         self.name = name
         self.age = age 
p1 = Person("Johne",36)         
print(p1.name)
print(p1.age)  

# object methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  

#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()