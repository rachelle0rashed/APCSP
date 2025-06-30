import random

# Enter your code here
num_rolls = 0
while True:
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    print("Rolled: " + str(roll_1) + " "+ str(roll_2))
    num_rolls += 1
    if (roll_1 == 1 and roll_2 == 1):
        break
print("It took you " + str(num_rolls) + " rolls")