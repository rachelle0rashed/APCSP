def get_index(max_length):
    while True:
        try:
            index = int(input("Enter an index (or -1 to stop): "))
            if index == -1:
                return index
            elif 0 <= index < max_length:
                return index
            else:
                print("Invalid index")
        except ValueError:
            print("Please enter a valid integer.")
def get_letter():
    while True: 
        letter = input("Enter a lowercase letter: ")
        if len(letter) != 1:
            print("Must be exactly one character!")
        elif not letter.islower():
            print("Character must be a lowercase letter!")
        else:
            return letter
            
            
# 1

word = input("Enter a word: ")
word_list = list(word)

while True:
    index = get_index(len(word))
    if index == -1:
        break
    letter = get_letter()
    word_list[index] = letter  
    word = "".join(word_list)

    print(word)