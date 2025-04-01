
# Approach:-

## Fixing Circular Import Issue

To fix the circular import issue between `module_a.py` and `module_b.py`, you can use local imports within functions to delay the import until it's actually needed. This prevents the circular import during the initial module load.

The circular import is resolved by moving the import statement inside the functions (`call_funcb()` and `call_funca()`), so imports only occur when the functions are called, preventing the circular dependency during the initial loading of the modules.

## Dynamic Module Loading

A program is implemented to dynamically import and execute a function from any module specified by the user. The script:
- Takes module name, function name, and argument as input.
- Converts the argument to a numeric type if possible.
- Imports the specified module and executes the function.
- Handles errors such as missing modules, missing functions, and invalid arguments.

## Custom Module with Exception Handling

### `calculator.py`:

- The `divide()` function tries to perform the division of `x` by `y`.
- It catches `ZeroDivisionError` for division by zero and returns a specific error message.
- It catches any other exceptions (like invalid input) and returns the error message.

### `main.py`:

- The script imports the `calculator` module and uses the `divide()` function.
- It demonstrates division by zero and invalid input (string and integer division) to show how exceptions are handled.

## Measuring Import Time

This script measures the time taken to import a module using different methods:

- **Single function import:** Imports just `sqrt` from the `math` module.
- **Full module import:** Imports the entire `math` module.
- **Time measurement:** Uses `time.time()` to measure and compare import times.

In general, importing specific functions can be slightly faster than importing the full module, but the difference is often negligible for small modules like `math`.

## Package Structure

### Package Structure:
The `my_package/` folder contains:
- `module_a.py` and `module_b.py` with functions `hello_from_a()` and `hello_from_b()`.
- `__init__.py` to make it a package and enable direct function access when imported.

### `setup.py`:
This configuration file enables package installation using `setuptools`. Metadata includes package name, version, description, and author details.

### Installing Locally:
Run `pip install .` to install the package locally, making it available for import in any script.

### Testing:
After installation, test the package by importing `my_package` and calling its functions.

## Investigate `sys.path`

Python searches for modules in predefined locations stored in `sys.path`. This script:
- Prints the original `sys.path`.
- Appends a custom directory for module imports.
- Imports and tests a module from the added path.

This technique is useful for loading modules from non-standard directories.

## Mocking in Unit Tests

`unittest.mock` allows simulating dependencies for isolated testing.

### Features:
- **Mock objects:** Fake objects that mimic real ones.
- **Patching:** Replace real objects with mocks during testing.
- **Assertions:** Verify function calls and arguments.

Example: Mocking `math.sqrt` to return `100` regardless of input and checking the expected value in a test case.

## Import Side Effects

Some modules execute code upon import. This script:
- Creates a module that prints a message when imported.
- Imports the module to demonstrate the effect.

## Investigate Python’s Import Caching

Python caches imported modules in `sys.modules`. This script:
- Imports a module and prints its entry from `sys.modules`.
- Shows how Python reuses cached modules to optimize performance.
- Uses `importlib.reload()` to reload a modified module.

---



