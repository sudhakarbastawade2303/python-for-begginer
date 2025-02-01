#Find the Largest of Three Numbers
#taking multple inputes
x, y, z = input("value: ").split()
print(x)
print(y)
print(z)

if x > y:
    print(x, "is largest")
elif y > x:
    print(y, "is largest")
else:
    print(z, "is largets")


