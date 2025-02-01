#count the ovwel in given string

data = input("enter the word: ").strip()
count = 0
ovwels = "aeiou"
for w in data:
    if w in ovwels:
        count += 1
print(count)
    
 #in line  if w in ovwels:   it check for w exist in ovwels