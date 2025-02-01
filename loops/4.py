#write multiplication table for givn number 
num = int(input("enter the number for multiplication table: "))

for i in range(1, 11):
    print(f"\n {num} * {i} = {num*i}\n")




#Note = The f in print(f"...") stands for f-string, which is short for formatted string literals.

#F-strings make it easy to embed variables directly into strings using {}.