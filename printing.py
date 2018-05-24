import imports
import main
import common


def print_results(dishes):
    chosen_dishes = []
    print("Znaleziono nastepujace potrawy:")
    i = 1
    for dish in dishes.keys():
        print(i, dish)
        chosen_dishes.append(dish)
        i += 1
    return chosen_dishes


# imports and prints files like welcome.txt end.txt
def graphics_display(graphic_file):
    with open(graphic_file, "r+") as file:
        lines = file.readlines()
        lines = ''.join(lines)
    print(lines)


def print_recipe(dish_name):
    
    print("\n***",dish_name.upper(),"***\n")
    
    dish_name = "dishes_details/" + dish_name + ".txt"
    with open(dish_name, "r") as file:
        lines = file.readlines()
        list_recipe = [item.strip("\n") for item in lines]
        for  line in list_recipe:
            print ("   ",line)
    print()


def print_all_short_recipes():
    print("\nChoose recipiec for :\n1. Breakfast\n2. Dinner\n3. Supper\n")
    choose = "0"
    while choose != "1" or choose != "2" or choose != "3":
        choose = input("\nWhat kind of meal do you choose?\n")
        if choose == "1":
            print("\n*BREAKFAST*\n")
            food_recipies = imports.import_recipes("breakfast.txt")
            break
        elif choose == "2":
            print("\n*DINER*\n")
            food_recipies = imports.import_recipes("dinner.txt")
            break
        elif choose == "3":
            print("\n*SUPPER*\n")
            food_recipies = imports.import_recipes("supper.txt")
            break
        else:
            print("try again")

    print_results(food_recipies)
    all_dishes = common.numeric_choose_dishes( food_recipies )
    dish_name = common.choose_dish(all_dishes, all_dishes)
    print_recipe(dish_name)   
   




  
