def main():
    try:
        number = int(input("Enter a non-negative whole number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    factorial = 1
    for value in range(2, number + 1):
        factorial *= value

    print("Factorial:", factorial)


if __name__ == "__main__":
    main()
