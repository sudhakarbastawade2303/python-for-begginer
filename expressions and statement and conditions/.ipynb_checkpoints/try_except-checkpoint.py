temp = input("enter the tempeature")
try:
    far = float(temp)
    cel = (far - 32.0) * 5.0 /9.0
    print(cel)
except:
    print("enter only number")