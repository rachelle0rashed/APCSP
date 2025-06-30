"""
 This program shows a simple way to crack a Caesar Cipher.

 The Caesar Cipher is not a secure encryption, because there's
 26 possible keys to try before cracking the cipher.
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Attempts every possible key until the message is successfully
# decrypted
# Returns the caesar key that the original message was encrypted with
def crack_caesar(encrypted_message, original_message):
    for i in range(len(ALPHABET)):
        decrypted_message_attempt = caesar_decrypt(encrypted_message, i)
        if decrypted_message_attempt == original_message:
            print("Cipher was cracked in only " + str(i) + " tries!")
            print("Correctly decrypted message: " + decrypted_message_attempt)
            return i
    return -1

def caesar_decrypt(encrypted_message, key):
    # Decrypting is the same process as encrypting,
    # the key just needs to shift the letters back instead of forward
    return caesar_encrypt(encrypted_message, -key)

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


original_message = input("Enter the message you would like to encrypt: ")
original_message = original_message.lower()

secret_key = int(input("Enter the number you'd like to shift each character by: "))

encrypted_message = caesar_encrypt(original_message, secret_key)
print("")
print("Encrypted message: " + encrypted_message)

print("")
print("Attempting to crack the encryption...")
print("")

cracked_key = crack_caesar(encrypted_message, original_message)

print("Correctly guessed the key: " + str(cracked_key))