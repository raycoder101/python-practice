#class test

class Animal:
    def __init__ (self, type, name):
        self.type = type
        self.name = name
    
    def speak(self):
        print("Hi I'm a", self.type, "and my name is", self.name)

    def moto(self):
        print("Life is short! Let's all just chillax!")


"""
# cat object initialized from Animal class
cat = Animal("cat", "Mimi")
cat.speak()

# dog object initialized from Dog class. 
dog = Dog("dog", "Cookie")
dog.speak()     # speak() method inherited from Animal class.
dog.dogSpeak()  # dogSpeak() method of Dog class.
"""