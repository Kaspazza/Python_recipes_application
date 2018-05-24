import printing
import note
from os import system
import common
import os.path


# choosing what to show on main menu
def main_menu_decision(authors):
    dishes_details_directory = "dishes_details/"
    decision = "0"
    while decision != "4":
        decision = input("what you want to do?\n")
        if decision == "1":
            final_dishes = common.meal_type_decision("find")
            printing.print_results(final_dishes)
            all_dishes = common.numeric_choose_dishes(final_dishes)
            choosen_dish = common.choose_dish(final_dishes, all_dishes)
            printing.print_recipe(choosen_dish, dishes_details_directory)
            common.deciding_to_add_note(choosen_dish)
            return
        elif decision == "2":
            food_recipes = printing.print_all_short_recipes()
            printing.print_results(food_recipes)
            all_dishes = common.numeric_choose_dishes(food_recipes)
            dish_name = common.choose_dish(all_dishes, all_dishes)
            print("\n***",dish_name.upper(),"***\n")
            printing.print_recipe(dish_name, "dishes_details/")
            if os.path.isfile("dishes_notes/"+ dish_name + ".txt") == True:
                print("    N O T E S \n")
                printing.print_recipe(dish_name, "dishes_notes/")
            
        elif decision == "3":
            printing.graphics_display(authors)


# main function
def main():
    welcome_screen = "graphics/welcome.txt"
    main_menu      = "graphics/menu.txt"
    end_screen     = "graphics/end.txt"
    authors        = "graphics/authors.txt"

    printing.graphics_display(welcome_screen)
    input("Click anything to start")
    system("clear")
    printing.graphics_display(main_menu)
    main_menu_decision(authors)
    printing.graphics_display(end_screen)


if __name__ == "__main__":
    main()
