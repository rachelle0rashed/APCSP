def add_one(x):
	# The result variable in this function is totally
	# different than the one in the sum function
	result = x + 1
	return result

def sum(x, y):
	result = x + y
	return result
	
x = add_one(8)
print(x)

y = add_one(10)
print(y)

a = sum(10, 20)
print(a)