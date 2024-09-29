'''
Objective: The aim of this assignment is to create a program that 
helps users make a shopping list.
Note: The goal of this is to be a program. The recommendation is to use a while loop 
that will allow the user to continue to add, remove, and print off 
their shopping list until they decide to "quit", also known as breaking the loop.
'''

# Task 1: Write a function that lets the user add items to a list.

shopping_list = []

def adding_to_the_list():
    shopping_list.append(add_item)
    print(f"--->> {add_item} has been added.")


# Task 2: Include a function to remove items from the list.

def removing_items():
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
        print(f"--->> {remove_item} has been removed.")
    else:
        print("Item is not on the list.")

# Task 3: Add a function that prints out the entire list in a formatted way.

def show():
    print(f"This is your shopping list:\n{"\n".join(shopping_list)}")

while True:
    try:
        print("\n1. Add item\n2. Remove item\n3. Show shopping list\n4. Exit")
        action = int(input("\n--- Your Shopping List ---\nWhat would you like to do? "))

        if action == 1:
            add_item = input("Please enter the item you want to add: ").lower()
            adding_to_the_list()
            
        
        elif action == 2:
            remove_item = input("Please enter the item you want to remove: ").lower()
            removing_items()

        elif action == 3:
            show()
            
        elif action == 4:
            print("Exit program. Goodbye!")
            break    

        else:
            print("Please enter a valid selection: (1,2,3,4)")

    except ValueError:
        print("Please enter the number of your selection.")
