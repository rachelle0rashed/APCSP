"""
 This program performs a lossy compression algorithm
 that simply removes all the vowels from the original text.
 
 The compressed text is significantly smaller, because it's removed
 several characters, but it is impossible to restore the original
 text, making it a lossy compression.

 You can see that, although the compressed form is missing some data,
 you are still able to read the resulting text with a little practice.
"""

def compute_space_saved(original, compress):
    original_size = len(original)
    compressed_size = len(compressed)
    
    space_saved = 1 - compressed_size / original_size
    percent_saved = space_saved * 100
    percent_saved = round(percent_saved * 100) / 100
    
    print("Original size: " + str(original_size))
    print("Compressed size: " + str(compressed_size))
    print("Percent Compressed: " + str(percent_saved) + "%")


# Returns true if the given letter is a vowel, false otherwise
def is_vowel(letter):
    vowels = "aeiou"
    return letter in vowels


# Returns a new String that is the same as the original but without any vowels
def remove_vowels(original):
    result = ""
    # Loop over the original String of text
    for letter in original:
        # If the current letter is not a vowel, add it to the result
        if not is_vowel(letter):
            result += letter

    # Return the resulting, vowelless text
    return result


original = input("Enter the text you would like to compress: ")

print("=======COMPRESSING=========")
compressed = remove_vowels(original)

print(compressed)
print('')

compute_space_saved(original, compressed)