#Write a program that asks for a number and checks if it is divisible by both 5 and 7.
num = float(input("enter number: "))

if num % 5 == 0:
    print(num, "is diviable by 5")
else:
    print("not divisiable")