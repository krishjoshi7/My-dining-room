""" This is the food menu 
    including starter, drinks
    alcoholic , non alcoholic"""

def food_items(menu_type):
    starter = {
            "gobi manchurian": 130,
            "gobi chilly": 140,
            "gobi 65": 160,
            "baby corn manchurian": 140,
            "baby corn pepper dry": 130,
            "mushroom manchurian": 130,
            "mushroom chilly": 150,
            "mushroom pepper dry": 160,
            "paneer manchurian": 170,
            "paneer chilly": 160,
            "paneer pepper dry": 160,
            "paneer 65": 160,
            }

    main_course ={
        "dal fry": 220,
        "panner masala": 240,
        "panner tikka": 230,
        "mutter panner": 250,
        "mix veg": 220,
        "bhindi masala": 210,
        "palak panner": 250,
        "aloo ghobhi": 180,
        "kaju panner": 260,
        "veg kofta": 240,
        "dal tadka": 220,
        "dal makhni": 250.
    }

    breads ={
        "pulka": 15,
        "rumali roti": 15,
        "parantha": 35,
        "tandoori roti":20,
        "butter roti":25,
        "butter naan":40,
        "garlic naan":50,
        "stuffed kulcha":50,
    }
    if (menu_type == "starter"):
        return starter, 
    elif(menu_type =="main course"):
        return main_course
    elif(menu_type =="breads"):
        return breads
    else:
        print("no menu found")
        return None


def print_menu(menu_type):
    hotel_menu = food_items(menu_type)
    print(hotel_menu)
    print(f'here is you {menu_type} menu')

# print_menu(menu_type)

def food_price(menu_type,my_oder):
    food_cost=0
    for item in my_oder:
        item_cost = menu_type[item]
        print(item_cost)
        food_cost + item_cost
        print("here is your bill")
        print(f'{item} /- rs {food_cost}')
    return food_cost



if __name__ =="__main__":
    print("here is list of menu")
    print("starter,main course,breads")
    print("chose your menu :- ")
    menu_type = input()
    my_oder = input()
    food_price(menu_type,my_oder)
  