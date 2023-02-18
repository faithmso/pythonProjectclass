"""
Write a program that prompts the user for a string and checks whether the string is a palindrome. (i.e the string reads
the same forward and backward.
"""


try:
    palindrome = input("Enter a name you think reads the same forward and backward ie palindrome: ")
    reversed_string = "".join(reversed(palindrome))
    if reversed_string == palindrome:

        print(f'The word {palindrome} is a palindrome.')

    else:
        print(f"The word {palindrome} is not a palindrome.")

except NameError:
    print("Enter a string.")





