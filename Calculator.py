# This function adds two numbers
# NAME: M McMahon

def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    """
    Divide x by y and return the result
    Args:
        x (float): First number
        y (float): Second number
    Returns:
        float: The quotient of x divided by y
    Raises:
        ValueError: If y is zero
    """
    # Convert inputs to float
    x = float(x)
    y = float(y)
    
    # Check for division by zero
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    
    # Return the quotient
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("You enter code for #2 here")
            # CODE HERE ENTERED
        elif choice == '3':
            print("You enter code for #3 here")
            
        elif choice == '4':
                    try:
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    except ValueError as e:
                        print(e)            
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
