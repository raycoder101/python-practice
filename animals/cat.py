from .animal import Animal

class Cat(Animal):
    def __init__ (self, type, name):
        self.type = type
        self.name = name
    
    def catSpeak(self):
        print("Meow! I'm a", self.type, "and my name is", self.name)