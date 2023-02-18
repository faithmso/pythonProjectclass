"""
Write a program that prompts the user for their age and checks whether they are old enough to vote (i.e, 18 years old or
older)
"""


try:
    age = float(input("Enter your age: "))

    if age >= 18:
        print(f'You are of age to vote.')

    else:
        print(f'You are too young to vote.')
except ValueError:
    print(f'Enter a valid integer or float.')
