import imports


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
    print()
    print("***",dish_name.upper(),"***")
    print()
    dish_name = "dishes_details/" + dish_name + ".txt"
    with open(dish_name, "r") as file:
        lines = file.readlines()
        list_recipe = [item.strip("\n") for item in lines]
        for  line in list_recipe:
            print ("   ",line)
    print()


def print_all_short_recipes():
    print("\nBREAKFEST")
    breakfest_recipies = imports.import_recipes("breakfast.txt")
    print_results(breakfest_recipies)
    print("\nDINNER")
    dinner_recipies = imports.import_recipes("dinner.txt")
    print_results(dinner_recipies)
    print("\nSUPPER")
    supper_recipies = imports.import_recipes("supper.txt")
    print_results(supper_recipies)
    print()
    




  
