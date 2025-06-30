import random
# Enter your code here
x = random.randint(1,100)
y = -1 
while y != x:
    try:
        y = int(input("Guess: "))
        if y > x:
            print("Too High")
        elif y < x:
            print("Too Low")
    except ValueError:
        print("Not a valid number")
print("Correct")/