# In this code, there's a Person class that has an attribute name, which gets 
# set when constructing the object. Fill in the blanks so that 1) when an instance 
# of the class is created, the attribute gets set correctly, and 2) when the greeting() 
# method is called, the greeting states the assigned name.

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return "hi, my name is {}".format(self.name) 

some_person = Person("Peter") 
print(some_person.greeting())
