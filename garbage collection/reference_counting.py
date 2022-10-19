# import sys,ctypes,gc
# a = 50
# # print(ctypes.c_long.from_address(id(a)).value)
# # print(sys.getrefcount(a))
# print(gc.get_referrers(50))
7


# import ctypes,sys
#
# my_var = 'hello python'
# my_var_address = id(my_var)
# print(sys.getrefcount(my_var))
# print(ctypes.c_long.from_address(my_var_address).value)
# print(sys.getrefcount(my_var_address))



import gc
i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
	x = { }
	x[i+1] = x
	print(x)

# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run



print("Creating cycles...")
for i in range(10):
	create_cycle()
collected = gc.collect() # or gc.collect(2)
print(f"Garbage collector: collected %d objects.{collected}")

create_cycle()
collected = gc.collect()

print(f"Garbage collector: collected %d objects{collected}")

print(gc.isenabled())
print(gc.get_threshold())