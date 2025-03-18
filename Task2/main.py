## Advanced Debugging Assignment
# Error Classification
# Identify the type of error in the following code snippets and fix them
for i in range(5):                
    print(i)

x = 10 / 0

def calculate_area(radius):
    return 2 * 3.14 * radius

# Debugging Complex Functions
# Debug the following function and correct the mistakes
def process_data(data):
    if len(data) == 0:
        return 0                 
    total = 0
    for item in data:
        try:
            total += int(item)  
        except ValueError:
            continue             
    return total / len(data)
print(process_data(['10', '20', 'abc', '30']))  
# O/P:- 20.0


# Advanced Debugging Challenge
# You’re given a function that fails intermittently. Investigate the bug and fix it
import random
def unreliable_function():
    number = random.choice([0, 1, 2])
    try:
        return 10 / number                       
    except ZeroDivisionError:
        return "Can't divide by 0"

for i in range(10):
    print(unreliable_function())


# Writing Debug-Friendly Code
# Refactor the following function to improve readability and add error handling
def calculate_discount(price, discount):
    try:
        # Ensure both price and discount are numbers
        price = float(price)
        discount = float(discount)

        # Validate discount range (0% to 100%)
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")

        # Calculate the discounted price
        final_price = price - (price * discount / 100)
        return round(final_price, 2)

    except ValueError:
        return "Error: Invalid input! Please enter numeric values for price and discount."

# Example Usage
print(calculate_discount(100, 10))    # Expected Output: 90.0
print(calculate_discount(100, "10%")) # Expected Output: Error message
print(calculate_discount(100, "10"))  # Expected Output: 90.0
print(calculate_discount("abc", 10))  # Expected Output: Error message
print(calculate_discount(100, -5))    # Expected Output: Error message


# Rubber Duck Debugging
# Explain the following code snippet step-by-step as if you’re teaching someone unfamiliar with coding
numbers = [1, 2, 3, 4, 5]          
result = 1                          
for num in numbers:                 
    result *= num                   
print("Product:", result)          

# Advanced Challenge: Debug a Multi-threaded Program
# Fix the race condition in the following code
import threading
counter = 0
counter_lock = threading.Lock()  

def increment():
    global counter
    for _ in range(100000):
        with counter_lock: 
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)       

#Expected O/P:- 20000

# Activity: Debug with Breakpoints
# Learn to use breakpoints in IDE (e.g., VSCode, PyCharm) to inspect variable states
import pdb
def divide(x, y):
    result = x / y
    pdb.set_trace()    
    return result
x = 10
y = 0
print(divide(x, y))
# (Pdb) p a  # Inspect the value of 'x'
# 10
# (Pdb) p b  # Inspect the value of 'y'
# 0
# (Pdb) n    # Step to the next line (this will raise a ZeroDivisionError)


# Memory Leaks and Performance Debugging
# Optimize the following code and fix potential memory leaks
import time
def optimized_function():
    result = (i * 2 for i in range(100000))  
    time.sleep(2)
    return result
print(sum(1 for _ in optimized_function()))  


# Unexpected None
# Debug why the function returns None
def add(a, b):
    return(a + b)
print(add(3, 4))                 
##No return statement in above code


# 10. Silent Failures
# Identify why the code doesn't raise an error
try:
    result = 10 / 0
except ZeroDivisionError:     
    pass
print("No error detected!")
