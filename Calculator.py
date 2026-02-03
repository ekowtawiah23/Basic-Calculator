def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed"
    return num1 / num2

def calculator():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in ('1', '2', '3', '4'):
        print("Invalid input. Please select a valid operation.")
        return

    try:
        num1 = float(input("Enter first number: ").strip())
        num2 = float(input("Enter second number: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    print(f"Result: {result}")

# Loop to allow multiple calculations
while True:
    calculator()
    again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the calculator!")
        break
