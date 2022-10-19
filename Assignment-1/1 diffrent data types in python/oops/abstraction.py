#abstraction is used to hide the functionality of the function from the user
#abstraction is used to hide irrelevant data/class in order to reduce the complexity 
#in python abstraction can be achieved by using abstract classes and interfaces

from abc import ABC,abstractmethod #here abc is abstract base class 

class Shape(ABC):
    @abstractmethod
    def print_area(self):
        pass
class Rectangle(Shape):
    type = "rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def print_area(self):
        return self.length*self.breadth
class hexagon(Shape):
    type = "hexagon"
    sides = 6
    def __init__(self):
        self.side = 3
    def print_area(self):
        return (3*(3**0.5)*(self.side**2)/2)
    
r = Rectangle()
print(r.print_area())
h = hexagon()
print(h.print_area())  