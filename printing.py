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


def print_recipe(dish_name, directory):

    print("\n***", dish_name.upper(), "***\n")

    dish_name = directory + dish_name + ".txt"
    with open(dish_name, "r") as file:
        lines = file.readlines()
        list_recipe = [item.strip("\n") for item in lines]
        for line in list_recipe:
            print ("   ",line)
    print()
