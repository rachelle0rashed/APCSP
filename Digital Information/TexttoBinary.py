"""
 This program encodes user input into binary data!
 Your job is to write the textToBinary function
"""

def text_to_binary(text):
    stringList = list(text)
    binaryList = []
    for i in range(len(text)):
        binaryList.append(str(decimal_to_binary(ord(stringList[i]))))
    translated_text = "".join(binaryList)
    return translated_text

# Converts a given decimal value into an 8 bit binary value
def decimal_to_binary(decimal_value):
    binary_base = 2
    num_bits_desired = 8
    binary_value = str(bin(decimal_value))[2:]
    
    while len(binary_value) < num_bits_desired:
        binary_value = "0" + binary_value
    
    return binary_value

text = input("Input the string you would like to encode: ")
binary = text_to_binary(text)

print(binary)