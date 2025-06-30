# Other Overflow Errors

"""
1. Rounding Error

In Python, a floating point number has a limited precision of 64 bits
which is about 16 digits. This can cause rounding off errors. Uncomment the 
first code segment to see this in action.

To uncomment a whole section - highlight the section and hit Shift (or Command) 
+ the "/" key.

"""


# Uncomment the below two lines and then run code. 
    
# x = 0.1 * 0.2 # should equal 0.02
# print(x)


"""
2. Exceeding the max and min numbers

Values smaller than the minimum are stored as 0, and values larger than the 
maximum are stored as +/- Infinity.

"""

# Uncomment the below three lines and then run code. 

# print(1e309);   # Infinity
# print(-1e309);   # -Infinity
# print(1e-324)  # 0