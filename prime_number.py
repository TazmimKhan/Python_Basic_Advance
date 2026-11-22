from math import isqrt


def main():
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if number < 2:
        print(number, "is not a prime number.")
        return

    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            print(number, "is not a prime number.")
            return

    print(number, "is a prime number.")


if __name__ == "__main__":
    main()
