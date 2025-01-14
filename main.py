# importing library 
import time

# importing local dependencies 
from oder import waiter
from menu import print_menu, food_price


def hotel():
    print("hello good afternoon")
    print("would you like me to bring menu?")
    qanda =input()
    if qanda =="yes":
        print("here is list of menu")
        print("starter,main course,breads")
        print("chose your menu :- ")
        menu_type = input()
        print_menu(menu_type)
        my_oder = waiter()
        print(my_oder)
        food_cost = food_price(menu_type,my_oder)
    elif qanda =="no": 
        print("waiting 10 seconds before asking for order again")
        time.sleep(10)
        print("would you like me to bring menu now ?")
        qanda =input()
        if qanda =="yes":
            print("here is list of menu")
            print("starter,main course,breads")
            print("chose your menu :- ")
            menu_type = input()
            print_menu(menu_type)
            my_oder = waiter()
            print(my_oder)
        elif qanda =="no":
            print("thank you for visiting")
    else:
        print("error occured")
    


if __name__ =="__main__":
    hol = hotel()
    print(hol)