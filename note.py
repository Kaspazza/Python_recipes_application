

def add_note(dish_name, text):
    dish_name = "note_dishes/" dish_name + ".txt"
    with open(dish_name, "a") as file:
        file.write(text + "\n")
    return dish_name


def print_note(dish_name):
    dish_name = "note_dishes/" + dish_name + ".txt"
    with open(dish_name, "r") as file:
        lines = file.readlines()
    print(lines)


print_note("tomato soup")