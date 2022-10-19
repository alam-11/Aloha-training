# polymorphism means having many forms 
# polymorphism means the same function name but being use for different types


class Parrot:
  
    def fly(self):
      print('Parrot can fly')

    def swim(self):
      print('Parrot can not swim')

class Penguin:
    def fly(self):
      print('Penguin can not fly')

    def swim(self):
      print('Penguin can swim')

def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)