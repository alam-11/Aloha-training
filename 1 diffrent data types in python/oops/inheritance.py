# When a class inherits all properties and behavior from the parent class is called inheritance. In such a case, the inherited class is a subclass and the latter class is the parent class.
# In child class, we can refer to parent class by using the super() function. The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.
class Bird(object):
    def __init__(self):
      print('Bird is ready')

    def whoisThis(self):
      print('Bird')

    def swim(self):
      print('Swim faster')

# child class
class Penguin(Bird):
    def __init__(self):
      # call super() function
      super().__init__()
      print('Penguin is ready')

    def whoisThis(self):
      print('Penguin')

    def run(self):
      print('Run faster')
      
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()