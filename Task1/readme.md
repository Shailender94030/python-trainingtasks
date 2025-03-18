VARIABLES, STATEMENTS, AND EXPRESSIONS: A LEARNING TASK
📝 VARIABLES
A variable is a storage location in memory that holds a value.
Example:

python
Copy
Edit
x = 5
ASSIGNING VALUES TO VARIABLES
python
Copy
Edit
x = 12
y = 2.14
z = 'Game'
print(type(x), type(y), type(z))  # Output: <class 'int'> <class 'float'> <class 'str'>

🧮 EXPRESSIONS
An expression is a combination of variables, values, and operators that evaluates to a result.
Example:

python
Copy
Edit
result = x + 3  # Evaluates to 8 if x = 5

📢 STATEMENTS
A statement is a line of code that performs an action, such as assigning a value or calling a function.
Example:

python
Copy
Edit
print("Hello, World!")

🔢 DATA TYPES
Data types specify what kind of value a variable can hold.

COMMON DATA TYPES:
python
Copy
Edit
a = 5         # Integer
b = 'Python'  # String
c = 3.14      # Float
print(type(a), type(b), type(c))

🔄 TYPE CONVERSIONS
Type conversion is the process of changing a value from one data type to another.
Example:

python
Copy
Edit
num = '123'
convert = int(num)
print(convert, type(convert))  # Output: 123 <class 'int'>

➕ OPERATORS AND OPERANDS
ARITHMETIC OPERATORS:
python
Copy
Edit
a = 2
b = 6

print("Addition:", a + b)          # 8
print("Subtraction:", a - b)       # -4
print("Multiplication:", a * b)    # 12
print("Division:", a / b)          # 0.3333
COMPARISON OPERATORS:
python
Copy
Edit
x = 5
y = 2

print("x > y:", x > y)   # True
print("x < y:", x < y)   # False
print("x == y:", x == y) # False
print("x != y:", x != y) # True
LOGICAL OPERATORS:
python
Copy
Edit
x = True  
y = False

print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False

🏗 FUNCTION CALLS
A function call executes a block of reusable code.

USING BUILT-IN FUNCTIONS:
python
Copy
Edit
num = [4, 2, 7, 1]
print(max(num) - min(num))  # Output: 6
FUNCTIONS AS OBJECTS:
python
Copy
Edit
greet = print
greet('Hello, World!')  # Output: Hello, World!

🔄 REASSIGNING VARIABLES
python
Copy
Edit
x = 9
y = 6
print("Initial values:", x, y)

x = 20
y = 10
print("Updated values:", x, y)

❌ VARIABLE NAMES AND KEYWORDS
RESERVED KEYWORDS (INVALID VARIABLES)
python
Copy
Edit
import keyword
print(keyword.kwlist)  # Lists all Python keywords

# Attempting to use a reserved keyword (SyntaxError)
try:
    def = 10  
    print(def)
except SyntaxError:
    print("You cannot use a reserved keyword as a variable name.")

🔍 CHOOSING THE RIGHT VARIABLE NAME
Using meaningful names improves readability.


🔴 BAD EXAMPLE:

python
Copy
Edit
a = 500  
b = 18  
c = a * (b / 100)  
d = a + c  
print(d)  

🟢 BETTER EXAMPLE:

python
Copy
Edit
principal_amount = 500  
interest_rate = 18  
interest = principal_amount * (interest_rate / 100)  
total_amount = principal_amount + interest  
print(total_amount)  

🏗 STATEMENTS VS EXPRESSIONS
✅ STATEMENT:

python
Copy
Edit
x = 5 + 3  # Assignment statement
print(x)   # Print statement
✅ EXPRESSION:

python
Copy
Edit
5 + 3  # Evaluates to 8

🔢 ORDER OF OPERATIONS
python
Copy
Edit
result = 2 + 3 * 4 ** 2 / 8
print(result)  # 8.0

🔁 REASSIGNMENT & UPDATING VARIABLES
REASSIGNING:
python
Copy
Edit
count = 10
print(count)  # Output: 10
count = 20
print(count)  # Output: 20
INCREMENTING AND DECREMENTING:
python
Copy
Edit
score = 100
score += 10
print(score)

score -= 5
print(score)  
