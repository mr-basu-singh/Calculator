try:
    # Take input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Show operation choices
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    # Perform operations using try-except for safe execution
    if choice == '1':
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"\nResult: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        print(f"\nResult: {num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print(f"\nResult: {num1} % {num2} = {num1 % num2}")
    elif choice == '6':
        print(f"\nResult: {num1} ^ {num2} = {num1 ** num2}")
    else:
        print("\nInvalid choice! Please select from 1 to 6.")

except ValueError:
    print("\nError: Please enter valid numbers.")

except ZeroDivisionError:
    print("\nError: Division or modulus by zero is not allowed.")

except Exception as e:
    print("\nUnexpected error occurred:", e)
