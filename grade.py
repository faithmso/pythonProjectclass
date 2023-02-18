"""
Write a program to prompt for a score between 0.0 and 1.0 if the score is out of range, print an error message.
If the score is between the range,print a grade using the following table
"""
score_grade = {
    "A" : 0.9,
    "B" : 0.8,
    "C" : 0.7,
    "D" : 0.6,

}

try:
    score = float(input("Enter a grade between 0.0 and 1.0: "))

    if score > 1.0:
        print(f"Score is out of range")

    elif score >= 0.9:
        print(f"Your scored an A")

    elif score >= 0.8:
        print(f"You scored a B")

    elif score >= 0.7:
        print(f"You scored a C")

    elif score >= 0.6:
        print(f"You scored a D")

    else:
        print(f"You scored an E")

except ValueError:
    print("Enter a valid integer or float")









