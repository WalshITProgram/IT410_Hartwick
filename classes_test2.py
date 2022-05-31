class Pet():
    """A simple class for representing a pet"""
    
    def __init__(self, name, age):
        """Initialize name and age variables/attributes"""
        self.name = name
        self.age = age

    def clean(self):
        """Represents the act of cleaning the pet"""
        print(self.name + " is clean!")
    
class Dog(Pet):
    """A simple class for representing a dog"""

    def __init__(self, name, age, breed):
        """Initialize name and age variables/attributes for the dog"""
        super().__init__(name, age)
        self.breed =  breed

    def placeDoginCarrier(self):
        """This represents placing the dog in a car carrier"""
        print(self.name + " is in the dog carrier!")

    def takeToVet(self):
        """Contains all of the tasks needed to get the dog to the vet"""
        self.placeDoginCarrier()
        self.__visitVet()
    
    def __visitVet(self):
        """Represents the act of taking the dog to the vet"""
        print(self.name + " is on their way to the vet!")

class Cat(Pet):
    """A simple class for representing a cat"""
    def __init__(self, name, age):
        """Initialize name and age variables/attributes for the cat"""
        super().__init__(name, age)


my_dog = Dog("Scout", 3, "German Shepherd")
print("My dogs name is: " + my_dog.name)
my_dog.clean()
print("My dogs breed is a " + my_dog.breed)

my_cat = Cat("Fluffy", 3)
print("My dogs name is: " + my_cat.name)