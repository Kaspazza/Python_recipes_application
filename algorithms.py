def get_dishes_by_all_components(components, dishes):

    # components - dict
    # dishes -dict{name:dict}

    result = {}

    for dish in dishes.keys():

        add = True

        for component in dishes[dish].keys():
            if component not in components.keys():
                add = False
            else:
                if dishes[dish][component] > components[component]:
                    add = False

        if add:
            result[dish] = dishes[dish]

    return result


def get_dishes_by_one_component(components, dishes):

    result = {}
    for dish in dishes.keys():

        dish_components = 0

        for component in dishes[dish].keys():
            if component in components:
                dish_components += 1

        if dish_components > 0:
            result[dish] = dishes[dish]

    return result


components = ["jajka", "mieso"]
components2 = {"jajka": 3, "chleb": 2}
dishes = {"jajecznica": {"jajka": 2, "chleb": 1}, "kotlet": {"mieso": 3, "smalec": 1}}

print(get_dishes_by_all_components(components2, dishes))
