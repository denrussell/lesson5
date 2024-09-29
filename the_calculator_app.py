'''
Objective: The aim of this assignment is to build a basic calculator that can perform 
addition, subtraction, multiplication, and division.

'''
# create the functions for each operation
def addition(a, b):
    result = a + b
    print(f"The sum is: {result}")

def subtraction(a, b):
    result = a - b
    print(f"The difference is: {result}")

def multiplication(a, b):
    result = a * b
    print(f"The product is: {result}")

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:  #added this to catch the zero error
        print("Error. Cannot divide by zero")
    else:
        print(f"The quotient is: {result: .2f}")  # formatted to 2 decimal places 

# Create the menu seclection
# print(f"1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")

while True:

    # Ask the user for the desired operation
    try:
        # Relocated this here so that it repeats.
        print(f"\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit\n")

        action = int(input("What would you like to do? "))

        # Create the conditions, then call the function
        if action == 1:
            a = int(input("Please enter the first number you want to add: "))
            b = int(input("Please enter the second number: "))
            addition(a, b)

        elif action == 2:
            a = int(input("Please enter the first number you want to subtract from: "))
            b = int(input("Please enter the second number: "))
            subtraction(a, b)

        elif action == 3:
            a = int(input("Please enter the first number you want to multiply: "))
            b = int(input("Please enter the second number: "))
            multiplication(a, b)

        elif action == 4:
            a = int(input("Please enter the first number you want to divide: "))
            b = int(input("Please enter the second number: "))
            division(a, b)
        
        elif action == 5:
            break

        else:  # when a number other than 1-5 is entered 
           print("Error. Please enter the number of your selection: (1)(2)(3)(4)(5)")
        

    except ValueError:  #when a string is entered rather than an integer
        print("Value error. Please enter the number of your selection: (1)(2)(3)(4)(5)")







        