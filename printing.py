def printResults(dishes):
    print("Znaleziono nastepujace potrawy:")
    for dish in dishes.keys():
        print(dish)
    print("sklad:")
        for key in dishes[dish]:
            print(key, dishes[dish][key], end ='')

