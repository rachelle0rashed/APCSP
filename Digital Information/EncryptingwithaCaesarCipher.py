"""
 This program encrypts alphabetical messages using a
 Caesar cipher.

 Given a secret key k, this algorithm simply shifts each alphabetical
 character in the message up by k characters. If the shift pushes
 a character past 'z', it wraps back around to the beginning and
 becomes 'a'.

 For example, "abcz" encrypted with a key of 1 would become "bcda"
"""
 
SECRET_KEY = 8
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(message, key):
    encrypted_result = ""
    
    for original_character in message:
    
        # If it's an alphabetical character, we'll compute the new
        # shifted character and add it to the encrypted result
        alphabetic_index = ALPHABET.find(original_character)
        if alphabetic_index >= 0:
            # Compute new index
            new_index = alphabetic_index + key
            new_index = new_index % len(ALPHABET)
            
            # Get the new character
            new_character = ALPHABET[new_index]
            
            # Add the new shifted character to the encrypted result
            encrypted_result += new_character
        
        # Otherwise we'll keep the original character
        else:
            encrypted_result += original_character
    return encrypted_result


original_message = input("Enter your message that you want to encrypt: ");
original_message = original_message.upper()

print("Encrypting with a Caesar Cipher...")
encrypted = caesar_encrypt(original_message, SECRET_KEY)
print("Done:")

print(encrypted)