#variable declaration in python

# Rules for variables
# * variable name must start with letter or the underscore
# * it can't start with underscore
# * it is case sensitive
# * reserved words cannot be used in naming


var = "hey"
_var = "hey1"  #can start with under score
# 1var = "hey2"    #error cannot start with numbers
var1 = "hey3"  #case sensitive
Var2 = "hey4"  #different case 
# print = "hey5" #cannot use the reserved words

#assigning a single value to multiple variables
a = b = c = 10
print([a,b,c])

#assigning different values to multiple variables
d,e,f = 3,45.5,"alam"
print([d,e,f])


# variable types in python 
# numeric,sequence,boolean,set,dict 

num = 132
string = "hey it's me nova"
flag = True
set1 = set("I am alam, my alias name is nova")
dict1 = {1:'A',2:'B',3:'C'}


# multiple names referencing the same object, is called a Shared Reference 
temp = 5
y = temp

#creating a variable of class type
class Demo:
    def __init__(self,text):
        self.text  = text
obj1 = Demo("this is demo")
print(obj1.text)

#type casting:-
#implicit type conversion:- python converts data type into another data type automatically

integer  = 7
floating = 5.88
addition = integer + floating
print(addition,type(addition))
#explicit type casting:- user manually typecaste
num1 = 5
print(type(num1))
num1 = float(num1)
print(type(num1))
num1 = str(num1)
print(type(num1))

#unpacking of collections

def print_seperately(a,b,c):
    print(a)
    print(b)
    print(c)

li = [1,2,3]
print_seperately(*li) # here * will unpack the list

#packing

def makelist(*args):
    return (list(args))
print(makelist(1,4,3,2,2))  #by default all the values will be tuple 

# unpacking the dictionary 
def unpack_dict(a,b,c):
    print(a,b,c)
dict2 = {'a':11,'b':22,'c':33}
unpack_dict(**dict2)

#packing the dictionary 

def pack_dict(**args):
    for key in args:
        print(key,args[key])
pack_dict(name="nova",roll="32",skills="python")


#scopes in python


#global variables are declared outside the funtion and can be used anywhere in the program 
#local variables are declared and used inside the funcition it's scope is local it cannot be used outside the function

def func():
    print(f) #accessing the global variable
func()
#global keyword allows to make the variable accessible outiside of the current scope it is used to create global variables from a non-global scope
x = 15
def change():
    global x
    x = x+5
    print(x)
change()

#nonlocal keyword is used in the case of nested funtions 
#it works similar to the global but rather than global this keywords declares a variable to point to the variable of outside enclosing function,in case of nested function

print("value of a using nonlocal is: ")
def outer():
    a = 5
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)
outer()

print("value of a without using nonlocal is: ")
def outer():
    a = 5
    def inner():
        a = 10
    inner()
    print(a)
outer()