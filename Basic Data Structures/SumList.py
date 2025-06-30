"""
This program will use for loops to go through elements in a list
and sum them up.
"""

numbers = [8, 4, 31, 56, 19]

# Create the sum outside the list
sum = 0

# Loop through all elements in the list
for i in range(len(numbers)):
    # add to the sum
    sum += numbers[i]

# Print the results
print(sum)