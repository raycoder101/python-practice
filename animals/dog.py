from .animal import Animal

class Dog(Animal):
    def __init__ (self, type, name):
        self.type = type
        self.name = name
    
    def dogSpeak(self):
        print("Woof! Woof! I'm a", self.type, "and my name is", self.name)