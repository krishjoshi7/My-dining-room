""" this will be the place for odering the food 
    the Waiter will take the oder 
    the Mr biller will do the billing """



def waiter():
    my_oder = []
    print("hello what would you like to oder :-")
    food_item =None
    while (food_item != "thank you"):
            print("please give the dishes to the me :-")
            food_item = input()
            if (food_item != "thank you"):
                 my_oder.append(food_item)
            else:
                 break
    return my_oder




def billing(my_oder):
    my_kart = []


if __name__ =="__main__":
     my_oder = waiter()
     print(my_oder)