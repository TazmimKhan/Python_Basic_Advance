first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if second_number == 0:
    print("Cannot divide by zero.")
else:
    quotient = first_number / second_number
    print("Quotient:", quotient)
