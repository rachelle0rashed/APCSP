"""
This program shows how indexing and slicing can be used with lists.
"""

# Creating an empty list:
my_list = []
print("Printing empty list:")
print(my_list)

# A variable can hold a whole list instead of just one value!
# Creating a list with things in it:
list_of_things = ["hi", 3, 4.8]
print("Printing list:")
print(list_of_things)

thing_zero = list_of_things[0]
thing_one = list_of_things[1]
thing_two = list_of_things[2]

print("0 Index Element: " + thing_zero)
print("1 Index Element: " + str(thing_one))
print("2 Index Element: " + str(thing_two))

print("Our Current list:")
print(list_of_things)

print("List length: " + str(len(list_of_things)))

# Unlike with a tuple, you can change a particular element in a list!
list_of_things[0] = 2

print("Changing element 0 to 2")
print(list_of_things)

# Get everything starting at thing 0 and going up to BUT NOT INCLUDING thing 2
print("Slice of things [0,2]")
print(list_of_things[0:2])

# This gets things 1 and 2
print("Slice of things [1,3]")
print(list_of_things[1:3])

# This gets everything from thing 1
# to the end.
print("Slice of things [1:]")
print(list_of_things[1:])

# This gets everything from the beginning up to but not including
# thing 2
print("Slice of things [:2]")
print(list_of_things[:2])

# This gets the last thing.
print("Slice of things [-1] (returns last element)")
print(list_of_things[-1])

# This gets the last two things.
print("Slice of things [-2:]")
print(list_of_things[-2:])

# This gets everything but the last thing.
print("Slice of things [:-1]")
print(list_of_things[:-1])