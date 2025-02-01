# 1. Name:
#      Jade Miller
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      A program based on the Monopoly game to tell if the user can build a hotel on Pennsylvania Avenue through a series of questions. 
# 4. What was the hardest part? Be as specific as possible.
#      For me the hardest part of the assignment was figuring out the rules of Monopoly while working on the assignment. It did help to do the flowchart but I had never played the game before so it took more time then it should to look through the rules before I could get started on the assignment.
# 5. How long did it take for you to complete the assignment?
#      5 hours


# Checking green properties
while True:
    user_land  = input('Do you own all the green properties? (y/n) ')

    if user_land in "nN":
        print(f"You cannot purchase a hotel until you own all the properties of a given color group.")
        quit()

    elif user_land in "yY":
        break

# Checking Pacific Avenue
available_houses = int(input('How many houses are there to purchase? '))
on_pac = int(input('What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))

if on_pac < 5:
    if on_pac + available_houses >= 4:
        needed_onpac =  4 - on_pac
        needed_houses = 4 - on_pac

        # Checking North Carolina Avenue
        on_nor = int(input('What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
        if on_nor < 5:
            if available_houses >= needed_houses:
                needed_nor = 4 - on_nor
                needed_houses += 4 - on_nor

                # Checking Pennsylvania Avenue
                on_pen =  int(input('What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))

                if on_pen < 5:
                    if available_houses >= needed_houses:
                        needed_onpen = 4 - on_pen
                        needed_houses += 4 - on_pen
                    else:
                        print(f"There are not enough houses available for purchase at this time.")
                        quit()
                elif on_pen == 5:
                    print(f"You cannot purchase a hotel if the property already has one.")
                    quit()
                else:
                    print("Invalid command.")
                    quit()
            else:
                print(f"There are not enough houses available for purchase at this time.")
                quit()
        elif on_nor == 5:
            print(f"Swap North Carolina's hotel with Pennsylvania's 4 houses.")
            quit()
        else:
            print("Invalid command.")
            quit()  
    else:
        print(f"There are not enough houses available for purchase at this time.")
        quit()
elif on_pac == 5:
    print(f"Swap Pacific's hotel with Pennsylvania's 4 houses.")
    quit()
else:
    print("Invalid command.")
    quit()

# Buying
user_cash = int(input('How much cash do you have to spend? $'))

if user_cash >= 200 * needed_houses:
    user_cash = user_cash -  200 * needed_houses
else:
    print(f"You do not have sufficient funds to purchase a hotel at this time.")
    quit()

available_hotels  = int(input('How many hotels are there to purchase? '))
if available_hotels >= 1:
    if user_cash >= 200:
        pass
    else:
        print(f"You do not have sufficient funds to purchase a hotel at this time.")
        quit()
else:
    print(f"There are not enough hotels available for purchase at this time.")
    quit()

price = (200 * needed_houses) + 200

# Checking Pennsylvania Avenue
if needed_nor >= 1 and needed_onpac >= 1:
    purchase_a = print(f"This will cost ${price}.\nPurchase 1 hotel and ${needed_houses} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {needed_nor} house(s) on North Carolina.\nPut {needed_onpac} house(s) on Pacific.")

elif needed_nor >= 1 and needed_onpac == 0:
    purchase_b = print(f"This will cost ${price}.\nPurchase 1 hotel and {needed_houses} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {needed_nor} house(s) on North Carolina.")

elif needed_nor == 0 and needed_onpac >= 1:
    purchase_c = print(f"This will cost ${price}.\nPurchase 1 hotel and {needed_houses} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {needed_onpac} house(s) on Pacific.")

elif needed_nor == 0 and needed_onpac == 0:
    purchase_d = print(f"This will cost ${price}.\nPurchase 1 hotel and {needed_houses} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.")