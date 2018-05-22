def printResults(dishes):
    print("Znaleziono nastepujace potrawy:")
    for dish in dishes.keys():
        print(dish)
    print("sklad:")
        for key in dishes[dish]:
            print(key, dishes[dish][key], end ='')


# imports and prints files like welcome.txt end.txt
def graphics_display(graphic_file):
    with open(graphic_file, "r+") as file:
        lines = file.readlines()
    print(lines)
