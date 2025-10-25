def addNumbers(firstNumber, secondNumber):
    return firstNumber + secondNumber

def main():
    print("This is a simple Addition Program\n")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # check for empty inputs
    if num1 == "" or num2 == "":
        print("Both inputs are required.")
        return

    # check if inputs are valid numbers (int or float, including negative)
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    result = addNumbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

main()
