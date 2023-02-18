"""
Write a program that takes in a list of integers and returns the largest number in the list that is also divisible by 3
"""


def largest_divisible_by_3(integers):
    largest = 0

    for item in integers:
        if item >= largest and item % 3 == 0:
            largest = item

    return largest


integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

results = largest_divisible_by_3(integers)
print(results)














