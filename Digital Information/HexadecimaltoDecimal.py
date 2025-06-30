"""
 This program converts hexadecimal values
 to decimal values
"""
 
NUMBER_BASE = 16;

"""
 Convert a given hexadecimal string
 into the equivalent decimal value.
 returns a number representing the decimal value
 of the hexadecimal string 
 Ex: "30F"
 
 Number:        3     0     F 
 Place:       16^2  16^1  16^0
 
 Place value:  256   16     1
 
 Compute decimal value: 3*(256) + 0*(16) + 15*(1) = 783
"""

def hex_to_decimal(hex_string):
    # Get the number of places in this hex number
    num_places = len(hex_string)
    
    # Get the current exponent starting with far left
    current_exponent = num_places - 1
    decimal_value = 0
    
    # Loop over each character of the hex string
    # and add the value of each place to the decimal value
    for i in range(len(hex_string)):
        # Get the value of this place (16 ^ current exponent)
        place_value = NUMBER_BASE ** current_exponent
        
        # Get the value of the current hex digit
        current_digit = hex_string[i:i+1]
        digit_value = int(current_digit, NUMBER_BASE)
        
        # Print out the value at this place
        print(str(digit_value) + " * (" + str(place_value) + ")", end="")
        if i != len(hex_string) - 1:
            print(" + ", end="")
        
        # Add this value to the decimal result
        decimal_value += digit_value * place_value
        
        # Decrease the exponent by one for the next place
        current_exponent -= 1
    
    print(" = " + str(decimal_value))
    return decimal_value

hex_string = input("Input a hexadecimal value: ")
decimal_value = hex_to_decimal(hex_string)
print(hex_string + " (hex) = " + str(decimal_value) + " (decimal)")