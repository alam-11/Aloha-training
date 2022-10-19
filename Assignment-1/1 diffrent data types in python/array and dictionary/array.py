# array is a collections of items stored at contiguous memory locations
# array in python can be created by importing array module

import array

# creating the array of integer type
int_array = array.array('i', [1, 23, 5])
print(int_array)
# creating the array of double type
double_array = array.array('d', [2.5, 3.5, 5.6])
print(double_array)
# inserting multiple element  in the array
int_array.insert(1, 4)
print(int_array)
# inserting element at the end of array using append
double_array.append(4.5)
print(double_array)
# removing the last element if parameter not passed
print(int_array.pop())
# slicing the array deleting a part of the array
sliced_int_array = int_array[2:]
print(sliced_int_array)
# finding the index of the particular element
print(int_array.index(2))
# updating the element of the array
int_array[1] = 55
