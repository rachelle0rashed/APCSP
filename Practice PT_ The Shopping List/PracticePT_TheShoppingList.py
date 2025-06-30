# what are we making??
print("Today, we are making some delicious pancakes!")

pantry = ["flour", "sugar", "baking powder", "salt", "eggs", "milk", "butter"]
extra_food = [] 


while True:
    ingredients = input("Please enter an ingredient ('done' when complete): ")
    if ingredients == "done":
        break
    extra_food.append(ingredients)

#check for missing ingredients
def missing_food(extra_food):
    missing_ingredients = []
    for item in extra_food:
        if item not in pantry:
            missing_ingredients.append(item)
    checking(missing_ingredients)
            
def checking(missing_ingredients):
    if len(missing_ingredients)>0:
        print("You need to go shopping!")
        print ("The following ingredients are missing")
        for ingredients in missing_ingredients:
            print(ingredients)
    else:
        print("It looks like you have everything to make your recipe!")
        
missing_food(extra_food)