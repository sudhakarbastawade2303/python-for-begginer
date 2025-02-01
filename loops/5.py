#find the factorial of given number
num = int(input("enter the number: "))
factorial =1
for i in range(1, num + 1):
    factorial *= i
print(f"factorial of {num} is {factorial}")