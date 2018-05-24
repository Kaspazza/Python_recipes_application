import imports
import main


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
    print("\nChoose recipiec for :\n1. Breakfast\n2. Dinner\n3. Su[pper\n")
    choose = "0"
    while choose != "1" or choose != "2" or choose != "3":
        choose = input("\nWhat kind of meal do you choose?\n")
        if choose == "1":
            print("\n*BREAKFAST*\n")
            breakfest_recipies = imports.import_recipes("breakfast.txt")
            print_results(breakfest_recipies)
            choose = "0"
            while choose != "1" or choose != "2" or choose != "3" or choose != "4" or choose != "5":
                choose = input("\nWhich dish?\n")
                if choose == "1":
                    choosen_dish = main.choose_dish(main.final_dishes, all_dishes)
                    printing.print_recipe(choosen_dish)
                if choose == "2":
                    pass
                if choose == "3":
                    pass
                if choose == "4":
                    pass
                if choose == "5":
                    pass
            break
        elif choose == "2":
            print("\n*DINER*\n")
            dinner_recipies = imports.import_recipes("dinner.txt")
            print_results(dinner_recipies)
            break
        elif choose == "3":
            print("\n*SUPPER*\n")
            supper_recipies = imports.import_recipes("supper.txt")
            print_results(supper_recipies)
            break
        else:
            print("XXX")    
   




  
