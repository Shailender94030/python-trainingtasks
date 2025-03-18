## 2.2 Values and Data Types
# Write a program that assigns different values to variables & prints the type of each variable
x = 12
y = 2.14
z = 'Game'
print(type(x), type(y), type(z))

## 2.3  Operators and Operands
a = 2
b = 6
sum = a + b
print("Addition:", sum)

# Subtraction
sub = a - b
print("Subtraction:", sub)

# Multiplication
multi = a * b
print("Multiplication:", multi)

# Division
div = a / b
print("Division:", div)

# Comparison Operators
x = 5
y = 2
print("x > y:", x > y)   # greater than
print("x < y:", x < y)   # less than
print("x == y:", x == y) # equal to
print("x != y:", x != y) # not equal to

# Logical Operations
x = True  
y = False
print("x and y:", x and y)  # True if both are True
print("x or y:", x or y)    # True if at least one is True
print("not x:", not x)      # Reverse the value of a

## 2.4 Function Calls
# Write a program that uses built-in functions inside expressions
num = [4, 2, 7, 1]
print(max(num) - min(num))

### 2.4.2 Functions are Objects; Parentheses Invoke Functions
# Assign a function to a variable, then call the function using the new vriable
greet = print
greet('Hello, World!')


## 2.5 Data Types
# Create variables of different types and print their types
a = 5
b = 'python'
c = 3.14
print(type(a), type(b), type(c))

## 2.6 Type Conversion Functions
# Convert variables between types and observe the results
num = '123'
convert = int(num)
print(convert, type(convert))   #result:123 <class 'int'>

## 2.7 Variables
# Assign values to variables, print them, and observe changes upon reassignment & assign initial values
x = 9
y = 6
print("Initial values:")
print("x =", x)
print("y =", y)

# After reassign values
x = 20
y = 10
print("After values:")
print("x =", x)
print("y =", y)
# Initial
x = 11
y = 6
# After 
x = 20
y = 12

## 2.8 Variable Names and Keywords
# Try using reserved keywords as variable names and observe the errors, & attempt to use reserved keywords as variable names
# Trying to use reserved keywords as variable names
# 'def' is a keyword in Python
try:
    def = 10  
    print(def)
except SyntaxError:
    print("You cannot use a reserved keyword as a variable name.")

# Fun fact for Listing All Python Keywords
import keyword
print(keyword.kwlist)


## 2.9 Choosing the Right Variable Name
# Rewrite a piece of code with meaningful variable names
a = 500  
b = 18  
c = a * (b / 100)  
d = a + c  
print(d)  


## 2.10 Statements and Expressions
#Identify statements and expressions in this code
x = 5 + 3
print(x)
Statement- x = 5 + 3, print(x)
Expression- 5 + 3

## 2.11 Order of Operations
#Write expressions using multiple operators to explore Python’s order of operations
result = 2 + 3 * 4 ** 2 / 8
print(result)

## 2.12 Reassignment

### 2.12.1 Developing Your Mental Model of How Python Evaluates
#Assign a value to a variable, reassign it, and observe the changes
count = 10
print(count) 
#o/p:-10  
count = 20
print(count)    
#o/p:-20

## 2.13 Updating Variables
#Increment and decrement variables using `+=` and `-=`
score = 100
score += 10
print(score) 
#o/p:-110      
score -= 5
print(score)
#o/p:-115      