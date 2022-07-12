#Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x) 

#class person 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#Variables p1
p1 = Person("John", 36)

#caling values
print(p1.name)
print(p1.age) 

#Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 