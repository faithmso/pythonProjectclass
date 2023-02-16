# Calculting pay by optaining the rate and the hours worked

hours_worked = float(input("Enter Hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = 0

print(f"Your pay is {pay}")


if hours_worked > 40:
    pay = (((hours_worked - 40) * (1.5 * rate_per_hour)) + (40 * rate_per_hour))
    print(f"Your pay is {pay}")

else:
    pay = hours_worked * rate_per_hour
    print(f"Your pay is {pay}")




