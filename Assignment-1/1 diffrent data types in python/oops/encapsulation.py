#encapsulation means wrapping data and the methods that works on data within one unit
#this puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data 


# private member:-it cannot be accessed outside the class not even in the derived class (use __ to define the private)
# protected member:- this can be accessed inside the class and the class to which it is inherited (use _ to define the protected)

class Computer(object):
    def __init__(self):
      self.__maxprice = 900
      
    def sell(self):
      print('Selling Price: {}'.format(self.__maxprice))
      
    def setMaxPrice(self, price):
      self.__maxprice = price
    
    
c = Computer()
c.sell()
# change the price
c.__maxprice = 1000  #can't access the maxprice directly
c.sell()
# using setter function
c.setMaxPrice(1000)
c.sell()