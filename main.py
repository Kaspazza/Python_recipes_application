import import_recipes.py
import algorithms.py


# imports and prints files like welcome.txt end.txt
def graphics_display(graphic_file):
    pass


#user inputs what he wants to see
def main_menu_decision():
    pass


def meal_type_decision():
    choose = input("You want receipts for breakfast, supper or dinner? (b,s,d)")

    if choose == "b":
        search_type("breakfast")

    elif choose == "s":
        search_type("supper")

    elif choose == "d":
        search_type("dinner")


def main():
    graphics_display("welcome.txt")
    main_menu_decision()

    pass


def search_type(file_type):

    choose = input("You want to search for receipts you can make with your \
    ingredients or receipts containing ingredient?(1 or 2)")

    if choose == "1":
        dishes = import_recipes.import_txt(file_type)
        components = pick_components()
        algorithms.get_dishes(components, dishes)

    elif choose =="2":
        dishes = import_recipes.import_txt(file_type)
        components = pick_components()


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


if __name__ == "__main__":
    main()
