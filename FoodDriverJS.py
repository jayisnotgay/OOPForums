from FoodExerciseJS import Food

# Function to create object list
def make_list():
    # Empty shopping_list list
    shopping_list = []

# User inputs number of items
    while True:
        n = eval(input("How many items are you going to buy? "))
        if n < 1:
            print("You have to buy at least one item")
        else:
            break

# user inputs name of item and amount in pounds, item appended to shopping_list list and returned
    for i in range(n):
        while True:
            item_name = str(input("Enter the name of the item: "))
            amt = eval(input("How many pounds? "))
            item = Food(item_name, amt)
            if item_name == "":
                print("You need to enter a valid name.")
            elif amt < 1:
                print("Amount has to be more than 0")
            else:
                break
        shopping_list.append(item)

    return shopping_list

# Displays all the item description on the shopping list items
def display(item_list):
    print("Here is the list of items you purchased: ")
    for i in range(len(item_list)):
        print(str(item_list[i].__str__())+"\n")

# Calculates the total order price of the shopping list items
def order_price(item_list):
    total = 0
    for i in range(len(item_list)):
        total += item_list[i].price_total()
        totalformat = "$ {:,.2f}".format(total)
    return totalformat

shopping_list = make_list()
display(shopping_list)

# Output of def order_price(item_list)
print(f"Total amount: {order_price(shopping_list)}")





