import time

# Virtual Assistant Lines

name = input("May I have a name please for the table beta ji: ")

input("Welcome to the restraunt " + str(name) +  ", our food is the best known here (Press enter)")

time.sleep(0.2)

input("Would you like a table for 1? (Press enter for yes)")

input("Alright seating you now... please look at our menu (Press enter to continue)")

print("Here is the Menu: \nBurger: $5\nDrink: $2\nDessert: $6\nFries: $3\n")

print("Please type Y or y if you want the item and if you dont want it simpily write NO")






# Checking if user wants food

burger = input("Would you like some burgers today?: ")

if burger == "y" or burger == "Y":
               
    burgerOrder = input("How many Burgers do you want: ")
                       
elif burger == "NO" :
    burgerOrder = 0
    print("No problem!")
   

drink = input("Would you like some drinks today?: ")

if drink == "y" or drink == "Y":
               
    drinkOrder = input("How many Drinks do you want: ")

elif drink == "NO" :
    drinkOrder = 0
    print("No problem!")

dessert = input("Would you like some dessert today?: ")

if dessert == "y" or dessert == "Y":
               
    dessertOrder = input("How many desserts do you want: ")

elif dessert == "NO" :
    dessertOrder = 0
    print("No problem!")

fries = input("Would you like some fries today?: ")

if fries == "y" or fries == "Y":
               
    friesOrder = input("How many fries do you want: ")

elif fries == "NO":
    friesOrder = 0
    print("No problem!")
   

# Constants

BURGER_PRICE = 5

DRINK_PRICE = 2

DESSERT_PRICE = 6

FRIES_PRICE = 3




# Adding up bill + saying goodbyes

total = int(burgerOrder) * BURGER_PRICE + int(drinkOrder) * DRINK_PRICE

total+= int(dessertOrder) * DESSERT_PRICE + int(friesOrder) * FRIES_PRICE

input("Enjoy the food! Brining you your bill soon (Press enter to continue)")

print("Your total bill is " + "$" + str(total))

input("Thanks for coming! (Press enter to leave)")

exit()
