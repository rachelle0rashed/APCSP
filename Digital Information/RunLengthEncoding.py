"""
 This program is an example of a simple lossless compression
 algorithm called run length encoding.

 Runs of characters (sequences of the same character repeating)
 in the original text are replaced with the single character and a
 count of how many times it occurs.

 For example, 
 "wwwwhaaaaaat?" 
 would be converted into
 "w4h1a6t1?1"
 Using 10 characters instead of 13, or a 1 - (10 / 13) = 23% compression rate

 This works well with data that contains several long runs of the same character.
"""

# Compresses the original String by building up a new String
# with each character and how many times it repeats in a given run.
# Returns the compressed text.
def compress(original):
    result = ""
    current_run_character = ""
    run_length = 0
    
    for i in range(len(original)):
        # If it's the start of the string, the current run starts with
        # the first character
        if i == 0:
            current_run_character = original[i]
            run_length = 1
        else:
            current_char = original[i]
            if current_char == current_run_character:
                run_length += 1
            else:
                # The run is over, add this run to the result
                result += current_run_character + str(run_length)
                
                # Reset the run variables
                current_run_character = current_char
                run_length = 1
  
    # Fencepost problem, the loop ended with the current run still going
    # Add the last run to the result
    result += current_run_character + str(run_length)
    
    # Return the compressed result text
    return result

# Decompresses the compressed Run Length Encoded text back
# into the original form.
def decompress(compressed_text):
    result = ""
    i = 0
    while i < len(compressed_text):
        # Get the current run character
        character = compressed_text[i]
        i += 1
        
        # Get the run length (which may have more than one digit)
        run_length = ""
        while i < len(compressed_text) and compressed_text[i].isdigit():
            run_length += compressed_text[i]
            i += 1
        
        # Add that many repetitions of the original character to the result
        result += character * int(run_length)
    return result

# Read in the original text
original_text = input("Enter the text you would like to compress: ")

print("Original Text: " + original_text)
print("")

# Compress the text
print("COMPRESSING...")

compressed_text = compress(original_text)
print("Compressed: " + compressed_text)
print("")

# Decompress the text
print("DECOMPRESSING...")

decompressed_text = decompress(compressed_text)
print("Decompressed: " + decompressed_text)
print("")

# Make sure the compression was lossless
if original_text == decompressed_text:
    print("Success! The decompressed text is the same as the original!")