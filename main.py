import imports.py
import algorithms.py
import printing.py


def pick_components():
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


def search_type(file_type):

    choose = input("You want to search for receipts you can make with your \
    ingredients or receipts containing ingredient?(1 or 2)")

    if choose == "1":
        dishes = import_recipes.import_recipes(file_type)
        components = pick_components()
        algorithms.get_dishes(components, dishes)

    elif choose =="2":
        dishes = import_recipes.import_recipes(file_type)
        components = pick_components()


def meal_type_decision():
    choose = input("You want receipts for breakfast, supper or dinner? (b,s,d)")

    if choose == "b":
        search_type("breakfast")

    elif choose == "s":
        search_type("supper")

    elif choose == "d":
        search_type("dinner")


#user inputs what he wants to see
def main_menu_decision():
    decision = "0"
    while decision != "3":
        decision = input("what you want to do?")
        if decision == "1":
            meal_type_decision()
        elif decision == "2":
            printing.graphics_display("authors")


def main():
    printing.graphics_display("welcome.txt")
    main_menu_decision()
    printing.graphics_display("end.txt")


if __name__ == "__main__":
    main()
