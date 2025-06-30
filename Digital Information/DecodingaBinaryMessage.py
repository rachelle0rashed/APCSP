"""
 This program converts a binary transmission into readable
 ASCII characters based on the ASCII encoding standard.
"""

# Decodes a given binary message into its equivalent ASCII characters
def ascii_decode(binary_message):
    # Initialize the resulting message
    result_message = ""
    # Loop over the binary message in chunks of 8 bits
    for i in range (0,len(binary_message), 8): 
        # Get the current byte of data from the message
        current_byte = binary_message[i:i+8]
        # Get the decimal value of that byte
        decimal_value = binary_to_decimal(current_byte);

        # Get the ascii character that corresponds to the decimal value
        ascii_character = str(chr(decimal_value))

        # Add that character to the resulting message
        result_message += ascii_character

    # Return the resulting message
    return result_message

# Uses a python builtin function to convert the binary string
# to a numeric decimal value.
def binary_to_decimal(binary_string):
    return int(binary_string, 2)

# Continually prompts the user for a binary transmission until
# a valid message is received. A valid message must contain full
# bytes of information, so if the message is not a multiple of 8 bits,
# pads 0s on the end of the message to make it a multiple of 8 bits.
# Also checks that the message contains only 0s and 1s.
def get_binary_transmission():
    while True:
        binary_message = input("Enter binary transmission: ")
            
        # Pad 0s on the end until the message is a multiple of 8 bits
        # allowing it to be decoded byte by byte
        while (len(binary_message) % 8 != 0):
            binary_message += "0"
            
        #if binary_message.search("[^01]") != -1:
         #   print("Error: Your message should contain only 1s and 0s.");
        #else:
        return binary_message
        
binary_message = get_binary_transmission()
text_message = ascii_decode(binary_message)

print("Message Received!")
print(text_message)