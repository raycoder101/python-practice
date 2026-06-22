# importing classes from the animals package
from animals import Animal, Dog, Cat

# horse object initialized from Animal class
horse = Animal("horse", "Charlie")
horse.speak()

# cat object initialized from Animal class
cat = Cat("cat", "Mimi")
cat.speak()     # speak() method inherited from Animal class.
cat.catSpeak()

# dog object initialized from Dog class. 
dog = Dog("dog", "Cookie")
dog.speak()     # speak() method inherited from Animal class.
dog.dogSpeak()  # dogSpeak() method of Dog class.
dog.moto()     # moto() method of Animal class.