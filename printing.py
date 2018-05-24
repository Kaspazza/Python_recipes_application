import imports
import main
import common


#
def print_results(dishes):
    chosen_dishes = []
    print("Znaleziono nastepujace potrawy:")
    i = 1
    for dish in dishes.keys():
        print(i, dish)
        chosen_dishes.append(dish)
        i += 1
    return chosen_dishes


# prints text from files
def graphics_display(graphic_file):
    with open(graphic_file, "r+") as file:
        lines = file.readlines()
        lines = ''.join(lines)
    print(lines)


def print_all_short_recipes():
    print("\nChoose recipiec for :\n1. Breakfast\n2. Dinner\n3. Supper\n")
    choose = "0"
    while choose != "1" or choose != "2" or choose != "3":
        choose = input("\nWhat kind of meal do you choose?\n")
        if choose == "1":
            print("\n*BREAKFAST*\n")
            food_recipes = imports.import_recipes("breakfast.txt")
            return food_recipes
        elif choose == "2":
            print("\n*DINER*\n")
            food_recipes = imports.import_recipes("dinner.txt")
            return food_recipes
        elif choose == "3":
            print("\n*SUPPER*\n")
            food_recipes = imports.import_recipes("supper.txt")
            return food_recipes
        else:
            print("try again")


# print("\n***",dish_name.upper(),"***\n")
def print_recipe(dish_name, directory):

    dish_name = directory + dish_name + ".txt"
    with open(dish_name, "r") as file:
        lines = file.readlines()
        list_recipe = [item.strip("\n") for item in lines]
        for line in list_recipe:
            print ("   ",line)
    print()
