dice_1 = int(input("First die? ")) 
print(dice_1)
got_dice = dice_1 == dice_1
dice_2 = int(input("Second die? "))
print(dice_2)
got_dice_2 = dice_2 == dice_1
rolled_doubles = got_dice and got_dice_2
print("Rolled doubles? " + str(rolled_doubles))