1. What is a Function?

A function is a reusable block of code that performs a specific task. It helps to organize code, reduce repetition, and make programs more modular and readable.

Why Use Functions?

Code Reusability – Write once, use multiple times.

Better Organization – Divides complex programs into smaller, manageable parts.

Improves Readability – Makes the code easier to understand.

Reduces Redundancy – Avoids repetition of the same code.

Facilitates Debugging – Debug a specific function without affecting other parts of the program.

2. Defining a Function

A function in Python is defined using the def keyword.

Syntax:

def function_name(parameters):
    """Optional Docstring"""
    # Function body
    return value  # Optional

def – Keyword to define a function.

function_name – The name of the function (follows naming rules: lowercase, underscores for spaces).

parameters – Inputs to the function (optional).

return – Sends back a result (optional).

3. Calling a Function

To execute a function, simply call it by its name and provide required arguments (if any).

Example: Function Without Parameters

def greet():
    print("Hello, welcome!")

greet()  # Function call

Output:

Hello, welcome!

Example: Function With Parameters

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

Output:

8

4. Function Parameters & Arguments

Parameters are placeholders in function definitions, and arguments are the actual values passed when calling the function.

Types of Arguments

Positional Arguments: Arguments passed in order.

def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Good Morning")  # Correct order

Keyword Arguments: Arguments passed with key-value pairs.

greet(name="Alice", message="Good Morning")

Default Arguments: Assigns a default value if no argument is passed.

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Uses default value
greet("Bob")  # Overwrites default

Variable-Length Arguments:

*args – Allows multiple positional arguments.

def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1, 2, 3, 4))  # Output: 10

**kwargs – Allows multiple keyword arguments.

def user_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
user_details(name="Alice", age=25, city="NY")

5. Return Statement in Functions

Functions can return values using the return keyword.

If no return is specified, the function returns None by default.

Example:

def square(num):
    return num * num

result = square(4)
print(result)  # Output: 16

6. Scope & Lifetime of Variables

Scope:

Local Variable: Defined inside a function and cannot be accessed outside it.

Global Variable: Defined outside functions and accessible throughout the program.

Use global Keyword: If you want to modify a global variable inside a function.

Example:

x = 10  # Global variable

def change_x():
    global x
    x = 20  # Modifies global variable

change_x()
print(x)  # Output: 20

7. Lambda (Anonymous) Functions

A lambda function is a small anonymous function using the lambda keyword.

Syntax:

lambda arguments: expression

Example:

square = lambda x: x * x
print(square(5))  # Output: 25

8. Recursion in Functions

A function calling itself is called recursion.

Example: Factorial Using Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

9. Function Best Practices

✅ Use descriptive function names.
✅ Keep functions small and focused.
✅ Use comments and docstrings ("""docstring""").
✅ Use return values instead of printing inside functions.
✅ Avoid using global variables inside functions.
✅ Use default arguments when appropriate.
✅ Use type hints for better readability (def add(a: int, b: int) -> int).

10. Summary

Feature

Description

Function Definition

def function_name(parameters):

Calling a Function

function_name(arguments)

Return Statement

return value

Parameters

Positional, Keyword, Default, Variable-length (*args, **kwargs)

Scope

Local, Global (global keyword)

Lambda Function

lambda args: expression

Recursion

A function calling itself

