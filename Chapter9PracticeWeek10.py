# problem 9-1
class Shirt():
    """Creates a basic shirt class"""
    def __init__(self, size, color):
        """Intalizes the shirts attributes"""
        self.size = size
        self.color = color
    
    def printSizeandColor(self):
        """This method prints out the size and color attributes"""
        print("The size of this shirt is a " + self.size)
        print("The color of this shirt is " + self.color)

my_shirt = Shirt("Medium", "Blue")
print("The attributes of myshirt are:")
print(my_shirt.size)
print(my_shirt.color)
my_shirt.printSizeandColor()

your_shirt = Shirt("Large", "Green")
print("The attributes of yourshirt are:")
print(your_shirt.size)
print(your_shirt.color)
your_shirt.printSizeandColor()

# problem 9-2 
class Shirt2():
    """This class creates a basic shirt class"""
    def __init__(self, size, color, quantity=1):
        """This constructor intalizes the different shirt attributes"""
        self.size = size
        self.color = color
        self.quantity = quantity
    def decreaseQuantity(self, value):
        """This methods decreases the quantity attribute with a specified value"""
        self.quantity = self.quantity - value
    def increaseQuantity(self, value):
        """This method decreases the quantity attribute with a specifed value  """
        self.quantity = self.quantity + value
        
my_shirt2 = Shirt2("Small", "Yellow", 4)
my_shirt2.increaseQuantity(3)
print(my_shirt2.quantity)
my_shirt2.increaseQuantity(2)
print(my_shirt2.quantity)
my_shirt2.increaseQuantity(4)
print(my_shirt2.quantity)
my_shirt2.decreaseQuantity(5)
print(my_shirt2.quantity)
my_shirt2.decreaseQuantity(6)
print(my_shirt2.quantity)

# problem 9-3 
class Clothing():
    """This class is  a base class for different articles of clothing """
    def __init__(self, size, color, quantity=1):
        """This constructor intalizes the different clothing attributes"""
        self.size = size
        self.color = color
        self.quantity = quantity
    def decreaseQuantity(self, value):
        """This methods decreases the quantity attribute with a specified value"""
        self.quantity = self.quantity - value
    def increaseQuantity(self, value):
        """This method decreases the quantity attribute with a specifed value  """
        self.quantity = self.quantity + value
    

class ShirtInherit(Clothing):
    def __init__(self, size, color, quantity, type, message):
        """Intalizes the ShirtInherit's attributes"""
        super().__init__(size, color, quantity)
        self.type = type
        self.message = message
    def printMessage(self):
        """Prints the message on the shirt"""
        print("The message on the shirt is: '" + self.message + "'")

graphic_shirt = ShirtInherit("Extra Large", "Green", 5, "Long-Sleeve", "Warning: may talk about roller coasters at any time")
graphic_shirt.increaseQuantity(5)
print(graphic_shirt.quantity)
graphic_shirt.printMessage()
#problem 9-4
class Pants(Clothing):
    """Creates a child class called pants that is an extension of the clothing class"""
    def __init__(self, size, color, quantity, fabricType, style):
        """Initalize the pants class attributes"""
        super().__init__(size, color, quantity)
        self.fabricType = fabricType
        self.style = style
    

