"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
import random

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0,9)
        random_passcode +=str(random_digit)
        return random_passcode
secret_passcode = generate_random_passcode()
    
# Write your code here

def guess_every_possible_passcode(secret_passcode):
    num_guesses = 0
    for first_dig in range(10):
        for second_dig in range(10):
            for third_dig in range(10):
                for fourth_dig in range(10):
                    current_guess = str(first_dig) + str(second_dig) + str(third_dig) + str(fourth_dig)
                    num_guess += 1
                    if is_correct(current_guess, secret_passcode):
                        print("Passcode: " + str(current_guess))
                        print("It took " + str(num_guess) + " guesses to find the correct passcode")
                    
(guess_every_possible_passcode(secret_passcode))