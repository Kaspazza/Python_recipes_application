import imports
import algorithms
import printing


# picking data for right algorithm
def pick_components(type):
    number_of_ingredients = input("How many ingredients you want to use?")
    if type == "1":
        components = {}
        for ingredients in range(int(number_of_ingredients)):
            ingredient = input("Pick ingredient")
            quantity   = input("Pick quantity")
            components[ingredient] = quantity

    elif type == "2":
        components = []
        for ingredients in range((number_of_ingredients)):
            ingredient = input("Pick ingredient")
            components.append(ingredient)

    return components


# getting dishes by choosen algorithm
def search_type(file_type):

    choose = "0"

    dishes = imports.import_recipes(file_type)
    while choose != "1" or choose != "2":
        choose = input("You want to search for receipts you can make with your ingredients or receipts containing ingredient?(1 or 2)")
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
    printing.printResults(final_dishes)
    print()

# choosing meal type
def meal_type_decision():

    choose = "0"

    while choose != "b" or choose != "s" or choose != "d":
        choose = input("You want receipts for breakfast, supper or dinner? (b,s,d)")
        if choose == "b":
            search_type("breakfast.txt")

        elif choose == "s":
            search_type("supper.txt")

        elif choose == "d":
            search_type("dinner.txt")
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
            printing.graphics_display("graphics/authors.txt")


# main function
def main():
    printing.graphics_display("graphics/welcome.txt")
    main_menu_decision()
    printing.graphics_display("graphics/end.txt")


if __name__ == "__main__":
    main()
