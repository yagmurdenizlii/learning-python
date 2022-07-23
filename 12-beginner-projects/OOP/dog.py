class Dog:

    #instanciates the object 
    #passes any arguments to this method
    #this method is always called
    def __init__(self, name, age):
        #creating an attribute of the class dog
        self.name = name
        self.age = age

    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    #a method is a function that goes inside a class
    #all methods have self as an argument
    def bark(self):
        print("bark")

d = Dog("Tim", 34) #creating a new instance of the class dog
d.bark() #calling the method on the dog object
print(type(d)) #will print <class '__main__.Dog'>
print(d.name)
print(d.get_name())

d.set_age(23)



