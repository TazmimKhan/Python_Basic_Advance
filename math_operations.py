def main():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print("Sum:", first_number + second_number)
    print("Difference:", first_number - second_number)
    print("Product:", first_number * second_number)

    if second_number == 0:
        print("Quotient: Cannot divide by zero.")
        print("Floor division: Cannot divide by zero.")
        print("Remainder: Cannot divide by zero.")
    else:
        print("Quotient:", first_number / second_number)
        print("Floor division:", first_number // second_number)
        print("Remainder:", first_number % second_number)

    try:
        print("Power:", first_number ** second_number)
    except ZeroDivisionError:
        print("Power: Zero cannot be raised to a negative power.")
    except OverflowError:
        print("Power: Result is too large to calculate.")


if __name__ == "__main__":
    main()
