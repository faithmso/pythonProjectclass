"""
Write a program that takes in a list of integers and returns the sum of all even numbers in the list.
"""


def sum_even_numbers(numbers):

    sum = 0

    for number in numbers:
        if number % 2 == 0:
            sum = sum + number

    return sum


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


results = sum_even_numbers(numbers)
print(results)
