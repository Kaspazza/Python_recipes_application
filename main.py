import imports.py
import algorithms.py
import printing.py


# picking data for right algorithm
def pick_components(type):
    number_of_ingredients = input("How many ingredients you want to use?")
    if type == "1":
        components = {}
        for ingredients in range(number_of_ingredients):
            ingredient = input("Pick ingredient")
            quantity   = input("Pick quantity")
            coponents[ingredient] = quantity

    elif type == "2":
        components = []
        for ingredients in range(number_of_ingredients):
            ingredient = input("Pick ingredient")
            components.append(ingredient)

    return components


# getting dishes by choosen algorithm
def search_type(file_type):

    choose = input("You want to search for receipts you can make with your \
    ingredients or receipts containing ingredient?(1 or 2)")

    dishes = import_recipes.import_recipes(file_type)
    components = pick_components(choose)
    algorithms.get_dishes(components, dishes, choose)


# choosing meal type
def meal_type_decision():
    choose = "0"
    while choose != "b" or choose != "s" or choose != "d":
        choose = input("You want receipts for breakfast, supper or dinner? (b,s,d)")
        if choose == "b":
            search_type("breakfast")

        elif choose == "s":
            search_type("supper")

        elif choose == "d":
            search_type("dinner")
        else:
            print("something went wrong, be sure you typed 'b', 's' or 'd'")


# choosing what to show on main menu
def main_menu_decision():
    decision = "0"
    while decision != "3":
        decision = input("what you want to do?")
        if decision == "1":
            meal_type_decision()
        elif decision == "2":
            printing.graphics_display("authors")


# main function
def main():
    printing.graphics_display("welcome.txt")
    main_menu_decision()
    printing.graphics_display("end.txt")


if __name__ == "__main__":
    main()
