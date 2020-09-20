class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        
        return "person: {}, age: {}" .format(self.name,self.age)
person = Person('Sarah', 25)

print(person)
