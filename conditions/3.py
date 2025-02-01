age = int(input("Enter age: "))
indian = input("enter True False: ").strip().lower()
if age <= 18:
    if indian == "True":
        boolean_value = True
        print("he can vote")
    else:
        print("not eligible")
else:
    print("he is unserage")
