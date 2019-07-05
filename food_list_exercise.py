#creating a list of food items for each day of the week 

mon_menu = ["white_rice", "stir_fry", "sesame_chicken", "beef", "fried_rice"]
tue_menu = ["bread", "stir_fry", "sesame_chicken", "beef", "fried_rice", "potatoes"]

user_selection = input("Enter Your Order: ")
user_selection = user_selection.lower()


#for x in mon_menu or tue_menu:
if user_selection not in mon_menu:
    print(user_selection,"is not available")
elif user_selection not in tue_menu:
    print(user_selection,"is not xxvailable")
else:
    print("your order of " + user_selection + " has been entered!")
            
#break

print()
