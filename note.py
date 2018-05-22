
def create_note(name):
    with open(name,"a") as file:
        lines = file.readlines()

def write_note(dish_name):
    with open(dish_name,"r+") as file:
        lines = file.readlines()
    box = [ item.strip("\n") for item in lines ]    

    box = []

    box. append(input(" your notes : "))

    for item in lines:
        x = item.strip("\n").split(",")
        box.append(x)
        
    with open(dish_name,"w") as file:
        for row in box:
            join_row =  ",".join(row) 
            file.write(join_row  + "\n")

    return dish_name

def print_note(dish_name):
    with open(dish_name,"r+") as file:
        lines = file.readlines()
    box = [ item.strip("\n") for item in lines ]  
    print(box)

#create_note("wwww")
print_note("tomato soup.txt\note_dishes")