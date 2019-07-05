#
# Order Entry program that reduces wait time at a restaurant
#
import time
import datetime


def lunch_time():

    print("Hello and welcome to SkyWay Wok!")
    time.sleep(1)
    print("Today's date and time: ", datetime.datetime.now())
    time.sleep(1)
    print("\n")
    print("Here's a list of Today's Menu!")
    print("Fried Rice, White Rice, Spicy Noodles, Sesame Chicken, Spicy Wings, Stir Fry")
    #my_list = [Fried_Rice, White_Rice, Spicy_Noodles, Sesame_Chicken, Spicy_Wings, Stir_Fry]
    order = input('would you like One, Two, or Three entrees?')

#
# The User is given a choice of one two or three entrees
#
    if str(order.lower()) == "one":
        one_entree()
    elif str(order.lower()) == "two":
        two_entree()
    elif str(order.lower()) == "three":
        three_entree()

    else:
        print("\n", order, " is not a valid selection")
#
#  The User inputs their selection
#


def one_entree():
    time.sleep(1)

    mon_menu = {"fried rice", "white rice", "spicy noodles", "sesame chicken", "spicy_wings", "stir_fry"}
    choice = input("Select Your Item:")

    if str(choice.lower()) not in mon_menu:
        print("\n", choice, "is not a valid selection," " Please select an item from the list")
    else:
        print("Your Order of " + choice + " Has been entered; Please proceed to cashier")


def two_entree():
    time.sleep(1)
    mon_menu = ["fried rice", "white rice", "Spicy Noodles", "Sesame Chicken", "Spicy Wings", "Stir Fry"]
    choice1 = input("Please Select your First Item:")

    if str(choice1.lower()) not in mon_menu:
        print("Item selected doesnt exist, Please Select an item from the list")

    choice2 = input("Please Select your second Item:")
    if str(choice2.lower()) not in mon_menu:
        print("Item selected doesnt exist, Please Select an item from the list")
    else:
        #print("Your Order of " + choice + " Has been entered; Please proceed to cashier")
        print("Your Order of " + choice1 + " and " + choice2 + " Has been entered")


def three_entree():
    choice1 = input("Please Select your First Item")
    choice2 = input("Please Select your second Item")
    choice3 = input("Please Select your third item")
    print("Your Order of " + choice1 + ", " + choice2 + " and " + choice3 + " Has been entered")
    print("Please proceed to cashier for payment")


lunch_time()
