# Calculator app

# functions of a simple calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1 ,n2):
    return n1 / n2

# making a dictionary of each operation in the dictionary which calls the desired fucntion depending on the operation
# symbol
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    for operation in operations:
        print(operation, end=" ")
    print("")
    continue_calc = True
    while continue_calc:
        operation = str(input("Select an operation: "))
        num2 = float(input("Enter the next number: "))
        # Setting which function to call from the operations dictionary based on user input
        function = operations[operation]
        # Running the desired operation using the numbers given by the user
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} equals {answer}")
        if str(input(f"Continue calculation with {answer}? Y, N: ")).lower() == "y":
            num1 = answer
        else:
            continue_calc = False
            calculator()

calculator()
