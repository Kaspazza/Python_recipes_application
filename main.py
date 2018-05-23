import imports
import algorithms
import printing
import note
from os import system


# picking data for right algorithm
def pick_components(type):
    number_of_ingredients = input("How many ingredients you want to use?\n")
    if type == "1":
        components = {}
        for ingredients in range(int(number_of_ingredients)):
            ingredient = input("Pick ingredient\n")
            quantity   = input("Pick quantity\n")
            components[ingredient] = quantity

    elif type == "2":
        components = []
        for ingredients in range(int(number_of_ingredients)):
            ingredient = input("Pick ingredient\n")
            components.append(ingredient)

    return components


# getting dishes by choosen algorithm
def search_type(file_type):

    choose = "0"

    dishes = imports.import_recipes(file_type)
    while choose != "1" or choose != "2":
        choose = input("Do You want to search for: \n 1.Receipts you can make with your ingredients \n 2.Receipts containing ingredient?(1 or 2)\n")
        if choose == "1":
            components = pick_components(choose)
            final_dishes = algorithms.get_dishes_by_all_components(components, dishes)
            break
        elif choose == "2":
            components = pick_components(choose)
            final_dishes = algorithms.get_dishes_by_one_component(components, dishes)
            break
        else:
            print("are you sure you picked 1 or 2? Try again!")
    return final_dishes

# choosing meal type
def meal_type_decision():

    choose = "0"

    while choose != "b" or choose != "s" or choose != "d":
        choose = input("You want receipts for: breakfast, supper or dinner? (b,s,d)\n")
        if choose == "b":
            final_dishes = search_type("breakfast.txt")
            return final_dishes
        elif choose == "s":
            final_dishes = search_type("supper.txt")
            return final_dishes
        elif choose == "d":
            final_dishes = search_type("dinner.txt")
            return final_dishes
        else:
            print("something went wrong, be sure you typed 'b', 's' or 'd'")


def choose_dish(final_dishes):
    dish_name = "niemamnie"
    while dish_name not in final_dishes:
        dish_name = input("choose which dish you want to see!\n")
    return dish_name


def deciding_to_add_note(choosen_dish):
    decision = "0"
    while decision != "y" or decision != "n":
        decision =  input("Do you want to add a note to your dish?(y/n)\n")
        if decision == "y":
            note_text = input("What you want to say than?\n")
            note.add_note(choosen_dish, note_text)
        else:
            return

# choosing what to show on main menu
def main_menu_decision(authors):
    decision = "0"
    while decision != "4":
        decision = input("what you want to do?\n")
        if decision == "1":
            final_dishes = meal_type_decision()
            printing.print_results(final_dishes)
            choosen_dish = choose_dish(final_dishes)
            printing.print_recipe(choosen_dish)
            deciding_to_add_note(choosen_dish)
            return
        elif decision == "3":
            printing.graphics_display(authors)
        elif decision == "2":
            pass

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
