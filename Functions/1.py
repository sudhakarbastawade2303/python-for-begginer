#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
def computepay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate

    return total_pay

# Get user input
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Compute and display pay
pay = computepay(hours, rate)
print(f"Total pay: ${pay:.2f}")
