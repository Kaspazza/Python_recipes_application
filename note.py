# adding notes
def add_note(dish_name, text):
    dish_name = "note_dishes/" + dish_name + ".txt"
    with open(dish_name, "a") as file:
        file.write(text + "\n")
    return dish_name
