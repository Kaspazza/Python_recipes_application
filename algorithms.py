def get_dishes(components, dishes):
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


components = {"jajka":3, "chleb":2}
dishes = {
    "jajecnica":{"jajka": 2},
    "kotlet": {"mieso": 3},
    "ziemniaki": {"jajka":3, "chleb":2}
}


res = getDishes(components,dishes)

print(res)
