"""
 This program simulates a computer with an 8-bit (1 byte) capacity
 that converts a decimal number into binary.
 
 A bit is shorthand for binary digit and is either a 0 or a 1.
 A byte is 8 bits. 
 
 Directions: Click Run Code and enter the numbers listed below. 
 Record the binary result.
 
 1. Enter number 248. Binary Result: 
 2. Enter number 252. Binary Result: 
 3. Enter number 254. Binary Result: 
 4. Enter number 255. Binary Result: 
 5. Enter number 256. Binary Result: 
 6. Enter number 257. Binary Result: 
 7. Enter any number over 255. Type Result Here: 
 8. What do you think is causing this error?  
 
 
 Takes a decimal value as a parameter and returns a String
 representing the equivalent binary value.
 
 Example: 13 (decimal) will be converted into 1101 (binary)

 The largest power of 2 that fits into 13 is 8, or 2^3.
 13 - 8 = 5. So 13 = 8 + 5, or 2^3 with 5 left over.

 The largest power of 2 that fits into 5 is 4, or 2^2.
 5 - 4 = 1. So 13 = 8 + 4 + 1, or 2^3 + 2^2 with 1 left over.

 1 already is a power of 2, 2^0.

 13 =   8 +   4 +   1
 13 = 2^3 + 2^2 + 2^0

 So in binary, we have 1 group of 8, 1 group of 4, 0 groups of 2,
 and 1 group of 1, or 1101

 13 (decimal) = 1101 (binary)
"""
import math

def decimal_to_binary(decimal_value):

    # Represents the resulting binary string
    binary_result = ""
    
    # Compute the starting exponent
    largest_power_of_2 = math.floor(math.log2(decimal_value))
    
    # Remainder starts off as the original value
    current_remainder = decimal_value
    
    # Starting from the largest exponent, count down the exponent to 0.
    # If the current power of 2 fits into the remainder, add a 1 to the binary result
    # and subtract the current power of 2 from the remainder
    # Otherwise, add a 0 to the binary result and the remainder remains the same.
    for current_exponent in range(largest_power_of_2, -1, -1):
        place_value = 2**current_exponent
        if place_value <= current_remainder:
            binary_result += "1"
            current_remainder -= place_value
        else:
            binary_result += "0"
        if len(binary_result) > 8:
            binary_result = "00000000"
            
    return binary_result

decimal_value = int(input("Decimal value = "))
binary_value = decimal_to_binary(decimal_value)
print(str(decimal_value) + " (dec) = " + str(binary_value) + " (bin)")