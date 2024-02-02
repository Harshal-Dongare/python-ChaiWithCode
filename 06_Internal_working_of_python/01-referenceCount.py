
# Creating a reference to an object
x = [1, 2, 3]

# Reference count of the list is now 1

# Creating another reference to the same object
y = x

# Reference count of the list is now 2

# Deleting one reference
del x

# Reference count of the list is now 1

# Deleting the remaining reference
del y

# Reference count of the list is now 0, and the memory can be reclaimed


#--------------------------------------------------------------------------

import sys

my_list = [1, 2, 3]

# return Number of references to this object
ref_count = sys.getrefcount(my_list) 
string_object_count = sys.getrefcount('dfdsf') # for a string object
bigInt_object_count = sys.getrefcount(4564564231432) # for big integers
mixed_object_count = sys.getrefcount('dfdsf45646')  # for mixed object

print(ref_count)                # output: 1
print(string_object_count)      # output: 3
print(bigInt_object_count)      # output: 3
print(mixed_object_count)      # output: 3

#----------------------------------------------------------------------------

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Modifying the list in-place
my_list[2] = 10       # Changing the value at index 2

print(my_list)        # Output: [1, 2, 10, 4, 5]

#------------------------------------------------------------------------------

# Copy operation
import copy

# using slice operator
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]

# using copy module
original_list2 = [1, 2, 3, 4, 5]
copied_list = copy.copy(original_list2)  # Shallow copy

# -------------------------------------------------------------------------

# equality check

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 is list2)  # output: false