# Assignment Codes
# Fix the circular import problem between module_a.py and module_b.py & resolve the circular need
# 1.module_a.py
def func_a():
    return "Function A"
def call_funcb():
    import b
    return b.func_b()
print(call_funcb())

# 2. module_b.py
def func_b():
    return "Function B"
def call_funca():
    import a
    return a.func_a()

# Dynamic Module Loading
# Write a program that dynamically imports and executes a function from any module specified by the user.
# Enter module name: math, Enter function name: sqrt, Enter argument: 25, Output: 5.0

import importlib
module_name = input('Enter module name')
function_name = input('Enter function name')
argument = input('Enter argument')

# Convert it to a number if possible:(float or integer) 
try:
    argument = float(argument) if '.' in argument else int(argument)
except ValueError:
    print("Invalid argument. Please enter a number.")
    exit()

try:
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    result = func(argument)
    print(f"Output: {result}")

except ModuleNotFoundError:
    print(f"Module '{module_name}' not found.")
except AttributeError:
    print(f"Function '{function_name}' not found in module '{module_name}'.")
except Exception as e:
    print(f"Error: {e}")


# Custom Module with Exception Handling
# Create a custom module calculator.py that handles division by zero and invalid inputs gracefully

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"

import calculator
x = 33
y = 66
result = calculator.divide(x,y)
print(result)


# Advanced Import Strategies
# Write a script that:
# Imports a module & Checks if a function exists.Executes it if available, otherwise gracefully handles the error

import importlib
mod_name = input('Enter module name')
func_name = input('Enter function name')
try:
    module = importlib.import_module(mod_name)
    if hasattr(module, func_name):
        func = getattr(module, func_name)
        result = func()
        print(f"Output: {result}")
    else:
        print(f"Function '{func_name}' not found in module '{mod_name}'.")
except ModuleNotFoundError:
    print(f"Module '{mod_name}' not found.")
except Exception as e:
    print(f"Error: {e}")


# Optimize Import Time
# Use time module to measure import time for different methods (single import vs. importing everything)
import time
start1 = time.time()
from math import sqrt
res = sqrt(25)
end1 = time.time()
print(f"Import time: {end1 - start1}")     

start2 = time.time()
import math
end2 = time.time()
print(f"Import time: {end2 - start2}")    


# Module Creation and Distribution
# Create a Python package structure with __init__.py. Write a setup.py to make it installable & Install your package locally
# Import and test your package.

def hello_from_a():
    return "Hello from module A"


def hello_from_b():
    return "Hello from module B"

# __init__.py- makes package
from .module_a import hello_from_a
from .module_b import hello_from_b

# setup.py-makes package install
from setuptools import setup, find_packages

setup(
    name="Jason_package", 
    version="0.1",  
    packages=find_packages(),  
    description="A sample package",  
    author="Your_Name", 
    author_email="your****.email@example.com",  
    classifiers=[
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",  
    ],
)

# To install the package locally, run: pip install 

# test_package.py after installing it will check the package
import my_package
print(my_package.hello_from_a())  
print(my_package.hello_from_b())  


# Investigate sys.path
# Explore sys.path and add a custom directory to import modules from an unconventional path
import sys
print("Original sys.path:", sys.path)
sys.path.append('/custom/path/to/modules')
import mymodule
print(mymodule.some_function())


# Mocking Modules for Testing
# Write a unit test for a function that imports a module. Use unittest.mock to mock the imported module
import unittest
from unittest import mock
import math
class TestMathSqrt(unittest.TestCase):
    def test_mock_sqrt(self):
        with mock.patch('math.sqrt', return_value=100):
            result = math.sqrt(25)  
            self.assertEqual(result, 100)  
if __name__ == '__main__':
    unittest.main()


# Import Side Effects
# Investigate modules that run code at import time. Create a module that prints something as soon as it’s imported
print("This runs on import!")
import mymodule
# At end of execution resulting that message being printed to the terminalas a o/p 


# Investigate Python’s Import Caching
# Explore sys.modules to understand how Python caches imports and how to reload modules
import sys
import mymodule
print(sys.modules['mymodule'])

