"""
Write a program that prompts the user for a number and checks whether the number is a prime number (i.e., only divisible
by 1 and itself)
"""

try:
    number = float(input("Enter a number: "))

    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print(f'{number} is not a prime number.')

    else:
        print(f'{number} is a prime number')

except ValueError:
    print("Enter a float or an integer.")


