def printResults(dishes):
    print("Znaleziono nastepujace potrawy:")
    i = 1
    for dish in dishes.keys():
        print(i, dish)
        i += 1


# imports and prints files like welcome.txt end.txt
def graphics_display(graphic_file):
    with open(graphic_file, "r+") as file:
        lines = file.readlines()
    print(lines)
