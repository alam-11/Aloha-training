# dictionary holds key:value pair


d = {1: 'alam', 2: 'nova', 3: 'faisal'}
d1 = d.copy()  # returns a copy of dictionary
print(d1)
d1.clear()  # removes all the element in the dictionary
print(d1)
print(d.keys())  # returns all the keys in the dictionary
print(d.values())  # return all the values in the dictionary
print(d.items())  # return list of tuples containing all the pairs
print(d.get(1))  # return a value for the specified key
print(d.pop(1))  # removes the element with specified key
d.update({3: "alam"})  # updates the value of specified key
