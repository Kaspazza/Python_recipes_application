def import_recipes(recipes_txt):
    with open(recipes_txt, "r+") as file:
        lines = file.readlines()
        recipies = [item.strip("\n").split(",") for item in lines]

    dishes = {}

    for i in range(0, len(recipies)-1, 2):
        dict_temp = {}
        for j in range(len(recipies[i+1])):
            temp = recipies[i+1][j]
            temp = temp.split(":")
            dict_temp[temp[0]] = temp[1]
        dishes[recipies[i][0]] = dict_temp
        i = i+1

    return dishes
