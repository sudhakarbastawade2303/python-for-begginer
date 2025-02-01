Loops in Python
Loops in Python allow you to repeat a block of code multiple times until a condition is met. Python has two main types of loops:

for loop (Used when you know how many times to loop)
while loop (Used when looping depends on a condition)

1️⃣ for Loop (Iterating Over a Sequence)
The for loop is used when you want to iterate over a sequence (like a list, tuple, string, or range).

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


Example 2: Using range() in a for Loop
The range() function generates numbers in a sequence.

for i in range(5):
    print(i)


Example 3: Looping with a Step Value

for i in range(1, 10, 2):  # Start at 1, go up to 10, increment by 2
    print(i)




2️⃣ while Loop (Runs Until a Condition Becomes False)
The while loop keeps running as long as the condition is True.


Example 4: Simple while Loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1  # Increase count by 1







3️⃣ Loop Control Statements
Python provides control statements to modify loop behavior:

break → Stops the loop immediately
continue → Skips the current iteration and moves to the next one
pass → Placeholder (does nothing)


Example 5: Using break (Stop the Loop)

for num in range(1, 10):
    if num == 5:
        break  # Stops the loop at 5
    print(num)



Example 6: Using continue (Skip an Iteration)

for num in range(1, 6):
    if num == 3:
        continue  # Skips printing 3
    print(num)


Example 7: Using pass (Do Nothing)

for num in range(1, 6):
    if num == 3:
        pass  # Placeholder for future code
    print(num)



4️⃣ Nested Loops (Loop Inside Another Loop)
A nested loop means a loop inside another loop.

Example 8: Nested for Loops (Multiplication Table)

for i in range(1, 4):  # Outer loop (rows)
    for j in range(1, 4):  # Inner loop (columns)
        print(i * j, end=" ")  # Print result in same line
    print()  # New line after inner loop
