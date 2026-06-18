# Python Interview Q&A - Complete Guide

## Interview Preparation Guide for Campus Placement
**Dayanand Sagar Engineering - 4th Year**

---

## 📑 Table of Contents

**Legend:** 🟢 Easy | 🟡 Medium | 🔴 Hard | ⏱️ Estimated Time

### BASIC LEVEL (Q1-Q20) ⏱️ 80-100 min
1. [🟢 What is Python?](#q1-what-is-python) ⏱️ 4 min
2. [🟢 Python Features](#q2-python-features) ⏱️ 5 min
3. [🟢 Interpreted vs Compiled](#q3-interpreted-vs-compiled) ⏱️ 5 min
4. [🟢 Python Data Types](#q4-python-data-types) ⏱️ 5 min
5. [🟢 List vs Tuple](#q5-list-vs-tuple) ⏱️ 5 min
6. [🟢 Dictionary and Set](#q6-dictionary-and-set) ⏱️ 5 min
7. [🟢 Mutable vs Immutable](#q7-mutable-vs-immutable) ⏱️ 5 min
8. [🟢 Pass by Reference or Value?](#q8-pass-by-reference-or-value) ⏱️ 5 min
9. [🟢 *args and **kwargs](#q9-args-and-kwargs) ⏱️ 5 min
10. [🟢 Lambda Functions](#q10-lambda-functions) ⏱️ 4 min
11. [🟢 List Comprehension](#q11-list-comprehension) ⏱️ 5 min
12. [🟢 Map, Filter, Reduce](#q12-map-filter-reduce) ⏱️ 5 min
13. [🟢 Modules and Packages](#q13-modules-and-packages) ⏱️ 5 min
14. [🟢 Exception Handling](#q14-exception-handling) ⏱️ 5 min
15. [🟢 File Operations](#q15-file-operations) ⏱️ 5 min
16. [🟢 `is` vs `==`](#q16-is-vs) ⏱️ 4 min
17. [🟢 Global vs Local Variables](#q17-global-vs-local-variables) ⏱️ 4 min
18. [🟢 `range()` vs `xrange()`](#q18-range-vs-xrange) ⏱️ 4 min
19. [🟢 String Methods](#q19-string-methods) ⏱️ 5 min
20. [🟢 `break`, `continue`, `pass`](#q20-break-continue-pass) ⏱️ 4 min

### INTERMEDIATE LEVEL (Q21-Q45) ⏱️ 115-135 min
21. [🟡 Decorators](#q21-decorators) ⏱️ 6 min
22. [🟡 Generators and Yield](#q22-generators-and-yield) ⏱️ 6 min
23. [🟡 Iterators and Iterables](#q23-iterators-and-iterables) ⏱️ 5 min
24. [🟡 Context Managers](#q24-context-managers) ⏱️ 5 min
25. [🟡 Shallow vs Deep Copy](#q25-shallow-vs-deep-copy) ⏱️ 5 min
26. [🟡 `__init__` vs `__new__`](#q26-__init__-vs-__new__) ⏱️ 5 min
27. [🟡 Pickling and Unpickling](#q27-pickling-and-unpickling) ⏱️ 5 min
28. [🟡 Multithreading vs Multiprocessing](#q28-multithreading-vs-multiprocessing) ⏱️ 6 min
29. [🟡 GIL (Global Interpreter Lock)](#q29-gil-global-interpreter-lock) ⏱️ 5 min
30. [🟡 Monkey Patching](#q30-monkey-patching) ⏱️ 4 min
31. [🟡 Static, Class, Instance Methods](#q31-static-class-instance-methods) ⏱️ 5 min
32. [🟡 Property Decorator](#q32-property-decorator) ⏱️ 5 min
33. [🟡 Python Memory Management](#q33-python-memory-management) ⏱️ 6 min
34. [🟡 Garbage Collection](#q34-garbage-collection) ⏱️ 5 min
35. [🟡 Regular Expressions](#q35-regular-expressions) ⏱️ 5 min
36. [🟡 `zip()` and `enumerate()`](#q36-zip-and-enumerate) ⏱️ 4 min
37. [🟡 `any()` and `all()`](#q37-any-and-all) ⏱️ 4 min
38. [🟡 List Slicing](#q38-list-slicing) ⏱️ 5 min
39. [🟡 Namespace and Scope](#q39-namespace-and-scope) ⏱️ 5 min
40. [🟡 `__str__` vs `__repr__`](#q40-__str__-vs-__repr__) ⏱️ 4 min
41. [🟡 JSON Operations](#q41-json-operations) ⏱️ 5 min
42. [🟡 Virtual Environment](#q42-virtual-environment) ⏱️ 5 min
43. [🟡 `*` and `/` in Function Parameters](#q43--and--in-function-parameters) ⏱️ 4 min
44. [🟡 Collections Module](#q44-collections-module) ⏱️ 5 min
45. [🟡 asyncio and Coroutines](#q45-asyncio-and-coroutines) ⏱️ 6 min

### ADVANCED LEVEL (Q46-Q60) ⏱️ 75-90 min
46. [🔴 Metaclasses](#q46-metaclasses) ⏱️ 6 min
47. [🔴 Descriptors](#q47-descriptors) ⏱️ 6 min
48. [🔴 Abstract Base Classes](#q48-abstract-base-classes) ⏱️ 5 min
49. [🔴 Method Resolution Order (MRO)](#q49-method-resolution-order-mro) ⏱️ 5 min
50. [🔴 Type Hints and Annotations](#q50-type-hints-and-annotations) ⏱️ 5 min
51. [🔴 Context Manager Protocol](#q51-context-manager-protocol) ⏱️ 5 min
52. [🔴 `__slots__`](#q52-__slots__) ⏱️ 5 min
53. [🔴 Weak References](#q53-weak-references) ⏱️ 5 min
54. [🔴 Python Optimization](#q54-python-optimization) ⏱️ 6 min
55. [🔴 Circular Imports](#q55-circular-imports) ⏱️ 5 min
56. [🔴 Context Variables](#q56-context-variables) ⏱️ 5 min
57. [🔴 Data Classes](#q57-data-classes) ⏱️ 5 min
58. [🔴 f-strings vs format()](#q58-f-strings-vs-format) ⏱️ 4 min
59. [🔴 EAFP vs LBYL](#q59-eafp-vs-lbyl) ⏱️ 5 min
60. [🔴 Python Design Patterns](#q60-python-design-patterns) ⏱️ 6 min

### Quick Reference Sections
- [📊 Key Comparison Tables](#-key-comparison-tables)
- [🎯 Top 15 Most Asked Questions](#-top-15-most-asked-questions)
- [📝 Python Syntax Cheat Sheet](#-python-syntax-cheat-sheet)
- [💡 Interview Tips](#-interview-tips)

---

## BASIC LEVEL QUESTIONS

### Q1. What is Python? 🟢

**Definition:**
Python is a high-level, interpreted, object-oriented programming language known for its simplicity and readability. Created by Guido van Rossum in 1991, Python emphasizes code readability with significant whitespace (indentation).

**Why it matters:**
Python is one of the most popular languages for web development, data science, machine learning, automation, and scripting. Understanding its philosophy helps in writing Pythonic code.

**Key Features:**
```python
# Simple and readable syntax
def greet(name):
    return f"Hello, {name}!"

# Dynamic typing - no need to declare types
x = 10        # int
x = "hello"   # now string - perfectly valid

# Multiple paradigms supported
# 1. Procedural
def calculate_sum(a, b):
    return a + b

# 2. Object-Oriented
class Calculator:
    def add(self, a, b):
        return a + b

# 3. Functional
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
```

**Python Philosophy (Zen of Python):**
```python
import this  # Try this in Python interpreter!
# Beautiful is better than ugly
# Explicit is better than implicit
# Simple is better than complex
# Readability counts
```

**Key Takeaway:**
Python prioritizes readability, simplicity, and versatility - making it ideal for beginners and experts alike.

---

### Q2. Python Features 🟢

**Definition:**
Python offers numerous features that make it popular and efficient for various applications.

**Key Features:**

1. **Easy to Learn and Read**
```python
# Python code reads like English
if age >= 18:
    print("You can vote")
```

2. **Interpreted Language**
```python
# No compilation needed, runs line by line
print("Hello")  # Executed immediately
```

3. **Dynamically Typed**
```python
x = 10      # int
x = "text"  # now string - no error
```

4. **Extensive Standard Library**
```python
import datetime, os, sys, json, re, math
# Rich built-in modules for common tasks
```

5. **Cross-Platform**
```python
# Same code runs on Windows, Mac, Linux
import platform
print(platform.system())  # Windows/Linux/Darwin
```

6. **Object-Oriented**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"
```

7. **Large Community and Libraries**
```python
# Rich ecosystem: numpy, pandas, flask, django, tensorflow
import numpy as np
import pandas as pd
```

**Key Takeaway:**
Python combines simplicity, power, and versatility with a rich ecosystem, making it suitable for diverse applications.

---

### Q3. Interpreted vs Compiled 🟢

**Definition:**
- **Interpreted**: Code executed line by line by an interpreter (Python, JavaScript)
- **Compiled**: Code translated to machine code before execution (C, C++, Java)

**Why it matters:**
Understanding execution models helps in debugging, optimization, and choosing the right language for specific tasks.

**Comparison:**

| Aspect | Interpreted (Python) | Compiled (C/C++) |
|--------|---------------------|------------------|
| **Execution** | Line by line | All at once after compilation |
| **Speed** | Slower | Faster |
| **Debugging** | Easier (immediate feedback) | Harder (must recompile) |
| **Portability** | High (interpreter needed) | Low (platform-specific binary) |
| **Error Detection** | Runtime | Compile-time |

**Python Execution Process:**
```python
# 1. Source Code (.py file)
def add(a, b):
    return a + b

# 2. Bytecode (.pyc file) - automatically created
# Python compiles to bytecode first

# 3. Python Virtual Machine (PVM)
# Interprets bytecode and executes

# 4. Output
result = add(5, 3)
```

**Example:**
```python
# Error caught at runtime in Python
def divide(a, b):
    return a / b

# No error until this line executes
result = divide(10, 0)  # ZeroDivisionError at runtime

# In compiled language like C:
// Error might be caught at compile time or runtime depending on scenario
```

**Key Takeaway:**
Python is interpreted (with bytecode compilation), offering flexibility and ease of development at the cost of execution speed.

---

### Q4. Python Data Types 🟢

**Definition:**
Python has several built-in data types to store different kinds of values. Python is dynamically typed - type is determined at runtime.

**Built-in Data Types:**

```python
# 1. Numeric Types
integer = 10                    # int
floating = 10.5                 # float
complex_num = 3 + 4j           # complex

# 2. Sequence Types
string = "Hello"               # str (immutable)
list_data = [1, 2, 3]         # list (mutable)
tuple_data = (1, 2, 3)        # tuple (immutable)

# 3. Set Types
set_data = {1, 2, 3}          # set (mutable, unique)
frozen = frozenset([1, 2])    # frozenset (immutable)

# 4. Mapping Type
dictionary = {"key": "value"}  # dict (mutable)

# 5. Boolean Type
is_valid = True                # bool

# 6. None Type
nothing = None                 # NoneType

# 7. Binary Types
byte_data = b"hello"           # bytes (immutable)
bytearray_data = bytearray(5)  # bytearray (mutable)
```

**Type Checking:**
```python
x = 10
print(type(x))        # <class 'int'>
print(isinstance(x, int))  # True

# Dynamic typing
x = "hello"
print(type(x))        # <class 'str'>
```

**Type Conversion:**
```python
# Implicit
x = 10
y = 5.5
result = x + y  # 15.5 (int promoted to float)

# Explicit
num_str = "100"
num_int = int(num_str)      # 100
num_float = float(num_str)  # 100.0
str_num = str(123)          # "123"
```

**Key Takeaway:**
Python offers rich built-in data types with dynamic typing, automatic type conversion, and easy type checking.

---

### Q5. List vs Tuple 🟢

**Definition:**
- **List**: Mutable, ordered collection of items enclosed in `[]`
- **Tuple**: Immutable, ordered collection of items enclosed in `()`

**Why it matters:**
Choosing between list and tuple affects performance, memory usage, and data integrity.

**Comparison Table:**

| Feature | List | Tuple |
|---------|------|-------|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Mutable** | Yes | No |
| **Speed** | Slower | Faster |
| **Memory** | More | Less |
| **Methods** | Many (append, remove, etc.) | Few (count, index) |
| **Use Case** | Dynamic data | Fixed data, dict keys |

**Code Examples:**
```python
# List - Mutable
my_list = [1, 2, 3]
my_list[0] = 10         # OK
my_list.append(4)       # OK
my_list.remove(2)       # OK
print(my_list)          # [10, 3, 4]

# Tuple - Immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10      # TypeError: tuple object doesn't support item assignment
# my_tuple.append(4)    # AttributeError: no append method

# Tuple with one element (note the comma!)
single = (1,)           # Tuple
not_tuple = (1)         # This is just int 1

# Tuple unpacking
coordinates = (10, 20)
x, y = coordinates      # x=10, y=20

# Tuple as dictionary key (immutable required)
locations = {
    (0, 0): "origin",
    (1, 1): "point A"
}
```

**Performance Comparison:**
```python
import sys

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_data))   # 104 bytes
print(sys.getsizeof(tuple_data))  # 88 bytes

# Tuples are more memory efficient
```

**When to Use:**
```python
# Use List when:
# - Data changes frequently
# - Need to add/remove elements
shopping_cart = ["apple", "banana"]
shopping_cart.append("orange")

# Use Tuple when:
# - Data should not change
# - Dictionary keys
# - Function returns multiple values
def get_coordinates():
    return (10, 20)  # Immutable return

coordinates = {(0, 0): "home", (1, 1): "work"}  # Valid
# coordinates = {[0, 0]: "home"}  # Error: list not hashable
```

**Key Takeaway:**
Use lists for dynamic data that changes; use tuples for fixed data that shouldn't change - tuples are faster and use less memory.

---

### Q6. Dictionary and Set 🟢

**Definition:**
- **Dictionary**: Unordered collection of key-value pairs (mutable)
- **Set**: Unordered collection of unique elements (mutable)

**Dictionary Operations:**
```python
# Creating dictionaries
student = {"name": "Alice", "age": 20, "grade": "A"}
empty_dict = {}
dict_constructor = dict(name="Bob", age=22)

# Accessing values
print(student["name"])          # Alice
print(student.get("age"))       # 20
print(student.get("missing", "N/A"))  # N/A (default value)

# Adding/Updating
student["major"] = "CS"         # Add new key
student["age"] = 21             # Update existing

# Removing
del student["grade"]            # Remove key
popped = student.pop("major")   # Remove and return value
student.clear()                 # Remove all items

# Iteration
person = {"name": "John", "age": 30, "city": "NYC"}
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Useful methods
print(person.keys())            # dict_keys(['name', 'age', 'city'])
print(person.values())          # dict_values(['John', 30, 'NYC'])
print(person.items())           # dict_items([('name', 'John'), ...])
```

**Set Operations:**
```python
# Creating sets
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates empty dict, not set!
from_list = set([1, 2, 2, 3])  # {1, 2, 3} - duplicates removed

# Adding/Removing
numbers.add(6)                  # Add element
numbers.remove(3)               # Remove (raises KeyError if not found)
numbers.discard(10)             # Remove (no error if not found)
popped = numbers.pop()          # Remove and return arbitrary element

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2             # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2      # {3, 4}
difference = set1 - set2        # {1, 2}
symmetric_diff = set1 ^ set2    # {1, 2, 5, 6}

# Methods
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.issubset(set2))      # False
print(set1.issuperset({1, 2}))  # True

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}

# Remove duplicates from list
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))        # [1, 2, 3, 4]
```

**Key Takeaway:**
Dictionaries store key-value pairs with O(1) lookup; Sets store unique elements with fast membership testing and set operations.

---

### Q7. Mutable vs Immutable 🟢

**Definition:**
- **Mutable**: Objects that can be changed after creation (list, dict, set)
- **Immutable**: Objects that cannot be changed after creation (int, str, tuple)

**Why it matters:**
Understanding mutability prevents bugs related to unexpected data changes and helps in choosing appropriate data structures.

**Mutable Objects:**
```python
# List - Mutable
my_list = [1, 2, 3]
my_list[0] = 10         # Modifies original
my_list.append(4)       # Modifies original
print(my_list)          # [10, 2, 3, 4]

# Dictionary - Mutable
my_dict = {"a": 1}
my_dict["b"] = 2        # Modifies original
print(my_dict)          # {"a": 1, "b": 2}

# Set - Mutable
my_set = {1, 2, 3}
my_set.add(4)           # Modifies original
print(my_set)           # {1, 2, 3, 4}
```

**Immutable Objects:**
```python
# String - Immutable
text = "hello"
# text[0] = "H"         # TypeError: str object doesn't support item assignment
new_text = text.upper()  # Creates new string, doesn't modify original
print(text)              # "hello" (unchanged)
print(new_text)          # "HELLO"

# Tuple - Immutable
coords = (10, 20)
# coords[0] = 15        # TypeError

# Integer - Immutable
x = 10
x = x + 1               # Creates new int object, doesn't modify 10
```

**Important Gotcha - Mutable Default Arguments:**
```python
# BAD: Mutable default argument
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(add_item_bad(1))  # [1]
print(add_item_bad(2))  # [1, 2] - Unexpected! Same list used

# GOOD: Use None as default
def add_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_good(1))  # [1]
print(add_item_good(2))  # [2] - Expected! New list each time
```

**Reference vs Copy:**
```python
# Mutable - Reference
list1 = [1, 2, 3]
list2 = list1           # Reference, not copy
list2[0] = 10
print(list1)            # [10, 2, 3] - Original changed!

# To copy: use .copy() or list()
list3 = list1.copy()
list3[0] = 99
print(list1)            # [10, 2, 3] - Original unchanged

# Immutable - Always creates new object
a = 10
b = a
b = 20
print(a)                # 10 - Original unchanged
```

**Key Takeaway:**
Mutable objects can be changed in-place; immutable objects create new objects on modification. Beware of mutable default arguments!

---



### Q8. Pass by Reference or Value? 🟢

**Definition:**
Python uses "pass by object reference" (or "pass by assignment"). The behavior depends on whether the object is mutable or immutable.

**Why it matters:**
Understanding this prevents bugs related to unexpected function side effects and data modification.

**How it works:**
```python
# Immutable objects (int, str, tuple) - appears like pass by value
def modify_immutable(x):
    x = 100  # Creates new object, doesn't affect original
    print(f"Inside function: {x}")

num = 10
modify_immutable(num)
print(f"Outside function: {num}")  # Still 10

# Mutable objects (list, dict) - appears like pass by reference
def modify_mutable(lst):
    lst.append(4)  # Modifies original list
    print(f"Inside function: {lst}")

my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"Outside function: {my_list}")  # [1, 2, 3, 4] - Modified!

# Reassignment doesn't affect original (even for mutable)
def reassign_list(lst):
    lst = [99, 99]  # Creates new object, doesn't affect original
    print(f"Inside function after reassignment: {lst}")

my_list = [1, 2, 3]
reassign_list(my_list)
print(f"Outside after reassignment: {my_list}")  # [1, 2, 3] - Unchanged
```

**Key Takeaway:**
Python passes object references. Modifying mutable objects affects the original; reassignment creates a new object.

---

### Q13. Modules and Packages 🟢

**Definition:**
- **Module**: A Python file (.py) containing code (functions, classes, variables)
- **Package**: A directory containing multiple modules with an `__init__.py` file

**Why it matters:**
Modules and packages enable code organization, reusability, and namespace management in large projects.

**Module Usage:**
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b

# main.py
import my_module
print(my_module.greet("Alice"))
print(my_module.PI)

# Or specific imports
from my_module import greet, PI
print(greet("Bob"))

# Import with alias
import my_module as mm
print(mm.greet("Charlie"))
```

**Package Structure:**
```python
# Directory structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# Usage
import mypackage.module1
from mypackage.subpackage import module3
from mypackage import *  # imports what's in __init__.py

# __init__.py can initialize package
# mypackage/__init__.py
__all__ = ['module1', 'module2']
from .module1 import func1
```

**Built-in Modules:**
```python
import os  # Operating system interface
import sys  # System-specific parameters
import math  # Mathematical functions
import datetime  # Date and time
import json  # JSON encoder/decoder
import re  # Regular expressions
import random  # Random number generation

# Check module location
print(os.__file__)

# List module contents
print(dir(math))
```

**Key Takeaway:**
Modules are single Python files; packages are directories with `__init__.py`. Use imports to organize and reuse code.

---

### Q15. File Operations 🟢

**Definition:**
Python provides built-in functions and context managers for reading, writing, and manipulating files.

**Why it matters:**
File handling is essential for data processing, logging, configuration management, and persistence.

**File Modes:**
- `'r'`: Read (default)
- `'w'`: Write (overwrites)
- `'a'`: Append
- `'r+'`: Read and write
- `'b'`: Binary mode
- `'t'`: Text mode (default)

**Reading Files:**
```python
# Method 1: with statement (recommended)
with open('file.txt', 'r') as f:
    content = f.read()  # Read entire file
    print(content)

# Method 2: read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Method 3: readlines (all lines as list)
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

# Method 4: read specific number of characters
with open('file.txt', 'r') as f:
    chunk = f.read(100)  # Read first 100 chars
```

**Writing Files:**
```python
# Write mode (overwrites)
with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("Python is awesome!")

# Append mode
with open('output.txt', 'a') as f:
    f.write("\nAppending new line")

# Write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

**File Operations:**
```python
import os

# Check if file exists
if os.path.exists('file.txt'):
    print("File exists")

# Get file size
size = os.path.getsize('file.txt')
print(f"Size: {size} bytes")

# Rename file
os.rename('old_name.txt', 'new_name.txt')

# Delete file
os.remove('file.txt')

# Get current directory
print(os.getcwd())

# List directory contents
print(os.listdir('.'))
```

**Binary Files:**
```python
# Write binary
with open('data.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')

# Read binary
with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)
```

**Key Takeaway:**
Always use `with` statement for automatic file closing. Know different modes and methods for reading/writing.

---

### Q17. Global vs Local Variables 🟢

**Definition:**
- **Local variables**: Defined inside functions, accessible only within that function
- **Global variables**: Defined outside functions, accessible throughout the module

**Why it matters:**
Understanding scope prevents naming conflicts and helps write cleaner, more maintainable code.

**Variable Scope:**
```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)

my_function()
# print(local_var)  # Error: local_var not accessible outside function

# Modifying global variable
count = 0

def increment_wrong():
    count = count + 1  # Error: local variable referenced before assignment

def increment_correct():
    global count  # Declare we're using global variable
    count = count + 1

increment_correct()
print(count)  # 1
```

**LEGB Rule (Scope Resolution Order):**
```python
# L = Local, E = Enclosing, G = Global, B = Built-in

x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # local
    
    inner()
    print(x)  # enclosing

outer()
print(x)  # global

# Built-in
print(len([1, 2, 3]))  # len is built-in function
```

**nonlocal keyword:**
```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Refers to enclosing scope's x
        x = 20
    
    inner()
    print(x)  # 20 - modified by inner()

outer()
```

**Best Practices:**
```python
# AVOID global variables when possible
# BAD
counter = 0

def increment():
    global counter
    counter += 1

# GOOD - use parameters and return values
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
```

**Key Takeaway:**
Use local variables by default. Only use `global` when necessary. Prefer passing parameters and returning values.

---

### Q18. range() vs xrange() 🟢

**Definition:**
- **Python 2**: `range()` returns list, `xrange()` returns iterator
- **Python 3**: `range()` returns iterator (like Python 2's xrange), `xrange()` doesn't exist

**Why it matters:**
Understanding the difference is important for interviews that may ask about Python 2/3 differences and memory efficiency.

**Python 2 (Legacy):**
```python
# Python 2
range(5)   # [0, 1, 2, 3, 4] - Creates list in memory
xrange(5)  # xrange object - Iterator, memory efficient

# For large ranges, xrange is much more memory efficient
big_range = xrange(1000000)  # Minimal memory
big_list = range(1000000)    # Large memory footprint
```

**Python 3 (Current):**
```python
# Python 3
range(5)  # range(0, 5) - Iterator (like Python 2's xrange)
# xrange() doesn't exist - NameError

# range object is lazy
nums = range(1000000)  # Minimal memory
print(type(nums))      # <class 'range'>

# Convert to list if needed
nums_list = list(range(5))  # [0, 1, 2, 3, 4]
```

**Usage Examples:**
```python
# Basic usage
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Start, stop, step
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

# Reverse
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1

# Common patterns
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
indices = range(len(my_list))

# Memory check
import sys
print(sys.getsizeof(range(1000000)))  # Small (~48 bytes)
print(sys.getsizeof(list(range(1000000))))  # Large (~8MB)
```

**Key Takeaway:**
In Python 3, `range()` is memory-efficient iterator. `xrange()` doesn't exist. Use `range()` for all iteration needs.

---

### Q19. String Methods 🟢

**Definition:**
Python strings have numerous built-in methods for manipulation, searching, and formatting.

**Why it matters:**
String operations are fundamental in text processing, data cleaning, and formatting output.

**Common String Methods:**
```python
text = "  Hello, World!  "

# Case conversion
print(text.upper())       # "  HELLO, WORLD!  "
print(text.lower())       # "  hello, world!  "
print(text.title())       # "  Hello, World!  "
print(text.capitalize())  # "  hello, world!  "
print(text.swapcase())    # "  hELLO, wORLD!  "

# Whitespace removal
print(text.strip())       # "Hello, World!"
print(text.lstrip())      # "Hello, World!  "
print(text.rstrip())      # "  Hello, World!"

# Searching
print(text.find("World")) # 9 (index, -1 if not found)
print(text.index("World")) # 9 (raises ValueError if not found)
print(text.count("o"))    # 2
print(text.startswith("  Hello"))  # True
print(text.endswith("!  "))        # True

# Replacement
print(text.replace("World", "Python"))  # "  Hello, Python!  "

# Splitting and joining
words = "apple,banana,cherry".split(",")  # ['apple', 'banana', 'cherry']
joined = "-".join(words)                  # "apple-banana-cherry"

# Checking
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
print("   ".isspace())    # True

# Formatting
name = "Alice"
age = 25
# f-strings (Python 3.6+)
print(f"My name is {name} and I'm {age}")

# format method
print("My name is {} and I'm {}".format(name, age))

# Old style
print("My name is %s and I'm %d" % (name, age))

# Padding and alignment
print("test".center(10, '*'))  # "***test***"
print("test".ljust(10, '-'))   # "test------"
print("test".rjust(10, '-'))   # "------test"
print("42".zfill(5))           # "00042"

# Multiline strings
multiline = '''Line 1
Line 2
Line 3'''
lines = multiline.splitlines()  # ['Line 1', 'Line 2', 'Line 3']
```

**String Slicing:**
```python
text = "Python Programming"

print(text[0])      # 'P'
print(text[-1])     # 'g'
print(text[0:6])    # 'Python'
print(text[7:])     # 'Programming'
print(text[:6])     # 'Python'
print(text[::2])    # 'Pto rgamn' (every 2nd char)
print(text[::-1])   # 'gnimmargorP nohtyP' (reverse)
```

**Key Takeaway:**
Strings are immutable. All methods return new strings. Know common methods: strip, split, join, replace, find, format.

---

### Q20. break, continue, pass 🟢

**Definition:**
- **break**: Exits the loop immediately
- **continue**: Skips current iteration, continues with next
- **pass**: Does nothing, placeholder statement

**Why it matters:**
These control flow statements are essential for loop manipulation and handling specific conditions.

**break - Exit Loop:**
```python
# Find first even number
numbers = [1, 3, 5, 6, 7, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break  # Exit loop immediately
    print(f"Checking {num}")

# Output:
# Checking 1
# Checking 3
# Checking 5
# Found even number: 6

# Break with while
count = 0
while True:
    count += 1
    if count > 5:
        break
    print(count)

# Break in nested loops (only breaks innermost)
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"i={i}, j={j}")
```

**continue - Skip Iteration:**
```python
# Skip odd numbers
for num in range(10):
    if num % 2 != 0:
        continue  # Skip rest of iteration, go to next
    print(num)  # Only even numbers printed

# Skip negative numbers
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(num)  # Output: 1, 3, 5
```

**pass - Placeholder:**
```python
# Empty function (to be implemented later)
def future_function():
    pass  # TODO: implement this

# Empty class
class EmptyClass:
    pass

# Conditional placeholder
for num in range(10):
    if num % 2 == 0:
        pass  # TODO: handle even numbers
    else:
        print(f"{num} is odd")

# Can't have empty blocks in Python
if condition:
    pass  # Required if block is empty
```

**else with loops:**
```python
# else executes if loop completes normally (no break)
for num in [1, 3, 5, 7]:
    if num % 2 == 0:
        print("Found even number")
        break
else:
    print("No even number found")  # This executes

# With break
for num in [1, 2, 3, 4]:
    if num % 2 == 0:
        print("Found even number")
        break
else:
    print("No even number found")  # This doesn't execute
```

**Practical Examples:**
```python
# Search with break
def find_item(items, target):
    for item in items:
        if item == target:
            return f"Found {target}"
            break  # Unreachable, but shows intent
    return f"{target} not found"

# Validation with continue
def process_valid_data(data_list):
    results = []
    for data in data_list:
        if not validate(data):
            continue  # Skip invalid data
        results.append(process(data))
    return results

# Placeholder for future implementation
def complex_algorithm():
    pass  # Will implement this next sprint
```

**Key Takeaway:**
Use `break` to exit loops, `continue` to skip iterations, `pass` as placeholder. Loops can have `else` clause.

---
\n### Q21. Decorators 🟡

**Definition:**
Decorators are functions that modify the behavior of other functions or classes without changing their source code. They use the `@decorator_name` syntax.

**Why it matters:**
Decorators enable code reuse, separation of concerns, and cleaner syntax for cross-cutting concerns like logging, authentication, and caching.

**Basic Decorator:**
```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Equivalent to:
# say_hello = my_decorator(say_hello)
```

**Decorator with Arguments:**
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

**Practical Examples:**
```python
import time
from functools import wraps

# 1. Timing decorator
def timer(func):
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# 2. Logging decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(5, 3)
# Output:
# Calling add with args=(5, 3), kwargs={}
# add returned 8

# 3. Authentication decorator
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_profile():
    return "Profile data"

# 4. Memoization (caching)
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 5. Class decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Initializing database")

db1 = Database()  # Initializing database
db2 = Database()  # No output - returns same instance
print(db1 is db2)  # True
```

**Multiple Decorators:**
```python
@decorator1
@decorator2
def my_function():
    pass

# Equivalent to:
# my_function = decorator1(decorator2(my_function))
```

**Key Takeaway:**
Decorators provide elegant way to modify function behavior using @syntax, commonly used for logging, timing, authentication, and caching.

---



## INTERMEDIATE LEVEL QUESTIONS (CONTINUED)

### Q23. Iterators and Iterables 🟡

**Definition:**
- **Iterable**: Any object that can be looped over (has `__iter__()` method)
- **Iterator**: Object with `__iter__()` and `__next__()` that produces values one at a time

**Why it matters:**
Understanding iterators enables efficient memory usage and custom iterable objects.

**Code Example:**
```python
# Iterable vs Iterator
my_list = [1, 2, 3]
my_iter = iter(my_list)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
# print(next(my_iter))  # StopIteration

# Custom Iterator
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in Counter(1, 5):
    print(num)
```

**Key Takeaway:**
All iterators are iterables, but not all iterables are iterators. Use `iter()` and `next()`.

---

### Q24. Context Managers 🟡

**Definition:**
Manage resources using `with` statement via `__enter__` and `__exit__` methods.

**Why it matters:**
Ensures proper cleanup even when exceptions occur, prevents resource leaks.

**Code Example:**
```python
# Built-in context manager
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed

# Custom context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.db_name}")
        return False

with DatabaseConnection("mydb") as db:
    print("Using database")

# Using contextlib
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    start = time.time()
    yield
    print(f"{name} took {time.time() - start:.4f}s")

with timer("Operation"):
    time.sleep(0.1)
```

**Key Takeaway:**
Use `with` for resource management. Implement `__enter__`/`__exit__` or use `@contextmanager`.

---

### Q26. `__init__` vs `__new__` 🟡

**Definition:**
- `__new__`: Creates instance (runs first)
- `__init__`: Initializes instance (runs second)

**Code Example:**
```python
class MyClass:
    def __new__(cls, *args):
        print("__new__ called")
        return super().__new__(cls)
    
    def __init__(self, value):
        print("__init__ called")
        self.value = value

obj = MyClass(10)
# __new__ called
# __init__ called

# Singleton using __new__
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

**Key Takeaway:**
`__new__` creates, `__init__` initializes. Use `__new__` for singletons and immutable types.

---

### Q27. Pickling and Unpickling 🟡

**Definition:**
Serializing Python objects to bytes (pickle) and deserializing (unpickle).

**Code Example:**
```python
import pickle

# Pickle data
data = {'name': 'Alice', 'scores': [95, 87, 91]}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Unpickle data
with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
print(loaded)

# Pickle to/from bytes
pickled = pickle.dumps(data)
unpickled = pickle.loads(pickled)

# Custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 30)
pickled_person = pickle.dumps(person)
loaded_person = pickle.loads(pickled_person)
```

**Security Warning:** Never unpickle untrusted data - can execute arbitrary code!

**Key Takeaway:**
Use `dump/load` for files, `dumps/loads` for bytes. Pickle is Python-specific; use JSON for interoperability.

---

### Q30. Monkey Patching 🟡

**Definition:**
Dynamically modifying classes/modules at runtime.

**Code Example:**
```python
# Original class
class Calculator:
    def add(self, a, b):
        return a + b

# Monkey patch - add method
Calculator.multiply = lambda self, a, b: a * b

calc = Calculator()
print(calc.multiply(5, 3))  # 15

# Monkey patch - replace method
Calculator.add = lambda self, a, b: a + b + 100
print(calc.add(5, 3))  # 108

# For testing
from unittest.mock import patch

def fetch_api():
    return "real data"

with patch('__main__.fetch_api', return_value="mock data"):
    print(fetch_api())  # "mock data"
```

**Key Takeaway:**
Useful for testing and hotfixes. Use `unittest.mock` for safe patching. Avoid in production.

---

### Q34. Garbage Collection 🟡

**Definition:**
Python uses reference counting + cyclic GC to reclaim memory.

**Code Example:**
```python
import sys
import gc

# Reference counting
a = [1, 2, 3]
print(sys.getrefcount(a) - 1)  # 1

b = a
print(sys.getrefcount(a) - 1)  # 2

del b
print(sys.getrefcount(a) - 1)  # 1

# Garbage collector
print(gc.isenabled())  # True
print(gc.get_threshold())  # (700, 10, 10)

# Force collection
collected = gc.collect()
print(f"Collected {collected} objects")

# Track objects
all_objects = len(gc.get_objects())
print(f"Total tracked objects: {all_objects}")
```

**Key Takeaway:**
Automatic memory management via ref counting + GC. Use `gc.collect()` for manual control.

---

### Q37. `any()` and `all()` 🟡

**Definition:**
- `any()`: Returns True if at least one element is True
- `all()`: Returns True if all elements are True

**Code Example:**
```python
# any() - at least one True
numbers = [0, 1, 2, 3]
print(any(numbers))  # True (1, 2, 3 are truthy)
print(any([0, 0, 0]))  # False (all falsy)
print(any([]))  # False (empty)

# all() - all True
print(all([1, 2, 3]))  # True
print(all([1, 0, 3]))  # False (0 is falsy)
print(all([]))  # True (empty - vacuous truth)

# Practical examples
ages = [25, 30, 18, 22]
print(all(age >= 18 for age in ages))  # True

scores = [85, 92, 78, 95]
print(any(score > 90 for score in scores))  # True

# Check if string has digits
text = "hello123"
print(any(c.isdigit() for c in text))  # True

# Validate all emails
emails = ["a@b.com", "invalid", "c@d.com"]
print(all("@" in email for email in emails))  # False
```

**Key Takeaway:**
Use `any()` for "or" logic, `all()` for "and" logic. Work with iterables and generators.

---

### Q38. List Slicing 🟡

**Definition:**
Extract portions of lists using `[start:stop:step]` syntax.

**Code Example:**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:5])    # [2, 3, 4]
print(numbers[:5])     # [0, 1, 2, 3, 4]
print(numbers[5:])     # [5, 6, 7, 8, 9]
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)

# Negative indices
print(numbers[-3:])    # [7, 8, 9]
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6]
print(numbers[-5:-2])  # [5, 6, 7]

# Step parameter
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (odds)
print(numbers[::3])    # [0, 3, 6, 9] (every 3rd)

# Reverse
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-2])   # [9, 7, 5, 3, 1]

# Assignment
numbers[2:5] = [20, 30, 40]
print(numbers)

# Delete
del numbers[2:5]
print(numbers)

# Copy list
original = [1, 2, 3]
copy = original[:]  # Shallow copy
```

**Key Takeaway:**
Slicing syntax: `[start:stop:step]`. Negative indices count from end. `[::-1]` reverses.

---

### Q39. Namespace and Scope 🟡

**Definition:**
Namespace is a mapping of names to objects. Scope determines where a variable can be accessed.

**Code Example:**
```python
# LEGB Rule: Local, Enclosing, Global, Built-in
x = "global x"

def outer():
    x = "enclosing x"
    
    def inner():
        x = "local x"
        print(f"Inner: {x}")  # local x
    
    inner()
    print(f"Outer: {x}")  # enclosing x

outer()
print(f"Global: {x}")  # global x

# global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# nonlocal keyword
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)  # 20

outer()

# Namespaces
import sys
print(dir())  # Local namespace
print(dir(sys))  # Module namespace
print(dir(__builtins__))  # Built-in namespace
```

**Key Takeaway:**
LEGB rule determines scope resolution. Use `global` for module-level, `nonlocal` for enclosing scope.

---

### Q40. `__str__` vs `__repr__` 🟡

**Definition:**
- `__str__`: Human-readable string representation (for users)
- `__repr__`: Unambiguous string representation (for developers)

**Code Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 25)

print(str(person))   # Alice, 25 years old
print(repr(person))  # Person('Alice', 25)
print(person)        # Alice, 25 years old (uses __str__)

# In lists, repr is used
people = [person]
print(people)  # [Person('Alice', 25)]

# If only __repr__ defined
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(10, 20)
print(p)  # Point(10, 20)
print(str(p))  # Point(10, 20) (falls back to __repr__)
```

**Key Takeaway:**
`__str__` for readability, `__repr__` for debugging. Always define `__repr__`. `str()` falls back to `__repr__`.

---

### Q42. Virtual Environment 🟡

**Definition:**
Isolated Python environments with independent packages and dependencies.

**Why it matters:**
Prevents dependency conflicts, enables project-specific package versions.

**Code Example:**
```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Linux/Mac)
source myenv/bin/activate

# Install packages
pip install requests numpy

# List installed packages
pip list
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

**Using venv in Python:**
```python
# Check if in virtual environment
import sys
print(sys.prefix)  # Shows venv path if active

# Check Python version
print(sys.version)

# Check site-packages location
import site
print(site.getsitepackages())
```

**Best Practices:**
```bash
# .gitignore
myenv/
venv/
env/
*.pyc
__pycache__/

# Always use requirements.txt
pip freeze > requirements.txt

# Use venv per project
project1/venv/
project2/venv/
```

**Key Takeaway:**
Always use virtual environments for projects. Use `venv` module, activate before installing packages, track dependencies in `requirements.txt`.

---

### Q43. `*` and `/` in Function Parameters 🟡

**Definition:**
- `*`: Forces all parameters after it to be keyword-only
- `/`: Forces all parameters before it to be positional-only (Python 3.8+)

**Code Example:**
```python
# Keyword-only parameters (after *)
def greet(name, *, greeting="Hello", punctuation="!"):
    return f"{greeting} {name}{punctuation}"

print(greet("Alice"))  # Hello Alice!
print(greet("Bob", greeting="Hi"))  # Hi Bob!
# greet("Charlie", "Hey")  # Error: greeting must be keyword

# Positional-only parameters (before /)
def divide(a, b, /):
    return a / b

print(divide(10, 2))  # 5.0
# divide(a=10, b=2)  # Error: positional-only

# Combined
def func(pos_only, /, standard, *, kw_only):
    print(f"{pos_only}, {standard}, {kw_only}")

func(1, 2, kw_only=3)  # OK
func(1, standard=2, kw_only=3)  # OK
# func(pos_only=1, standard=2, kw_only=3)  # Error

# Practical example
def create_user(user_id, /, username, *, email, password):
    """
    user_id: must be positional
    username: can be positional or keyword
    email, password: must be keyword
    """
    return {
        'id': user_id,
        'username': username,
        'email': email,
        'password': password
    }

user = create_user(123, "alice", email="a@b.com", password="secret")
```

**Key Takeaway:**
Use `*` for keyword-only params (better readability), `/` for positional-only params (API clarity).

---

### Q45. asyncio and Coroutines 🟡

**Definition:**
Asynchronous programming framework for concurrent code using `async`/`await`.

**Why it matters:**
Enables efficient I/O-bound operations, concurrent task execution without threading overhead.

**Code Example:**
```python
import asyncio
import time

# Basic coroutine
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Run coroutine
asyncio.run(say_hello())

# Multiple concurrent tasks
async def fetch_data(id, delay):
    print(f"Fetching {id}...")
    await asyncio.sleep(delay)
    print(f"Fetched {id}")
    return f"Data {id}"

async def main():
    # Sequential (slow)
    await fetch_data(1, 1)
    await fetch_data(2, 1)
    # Takes 2 seconds
    
    # Concurrent (fast)
    task1 = asyncio.create_task(fetch_data(1, 1))
    task2 = asyncio.create_task(fetch_data(2, 1))
    await task1
    await task2
    # Takes 1 second

asyncio.run(main())

# Gather multiple tasks
async def main_gather():
    results = await asyncio.gather(
        fetch_data(1, 1),
        fetch_data(2, 1),
        fetch_data(3, 1)
    )
    print(results)  # ['Data 1', 'Data 2', 'Data 3']

asyncio.run(main_gather())

# Timeout
async def slow_operation():
    await asyncio.sleep(5)
    return "Done"

async def with_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(with_timeout())

# async for
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main_async_for():
    async for num in async_range(5):
        print(num)

asyncio.run(main_async_for())
```

**Key Takeaway:**
Use `async def` for coroutines, `await` to pause, `asyncio.run()` to execute. Great for I/O-bound concurrency.

---


---

## ADVANCED LEVEL QUESTIONS

### Q46. Metaclasses 🔴

**Definition:**
Metaclasses are classes of classes that define how classes behave. A class is an instance of a metaclass.

**Why it matters:**
Advanced topic for frameworks and libraries. Controls class creation behavior.

**Code Example:**
```python
# Everything in Python is an object, including classes
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
print(type(MyClass()))  # <class '__main__.MyClass'>

# Custom metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        # Add a class attribute automatically
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)
    
    def __call__(cls, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()  # Prints: Creating instance of MyClass
print(obj.created_by)  # Meta

# Singleton using metaclass
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

**Key Takeaway:**
Metaclasses control class creation. Use `type` as base. Rarely needed in application code.

---

### Q47. Descriptors 🔴

**Definition:**
Objects that define how attribute access is handled via `__get__`, `__set__`, `__delete__` methods.

**Code Example:**
```python
# Descriptor protocol
class Validator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)
    
    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be <= {self.max_value}")
        setattr(obj, self.name, value)

class Person:
    age = Validator(min_value=0, max_value=120)
    
    def __init__(self, age):
        self.age = age

p = Person(25)
print(p.age)  # 25
# p.age = -5  # ValueError
# p.age = 150  # ValueError

# property is a descriptor
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value
```

**Key Takeaway:**
Descriptors manage attribute access. `@property` uses descriptors. Advanced but powerful.

---

### Q48. Abstract Base Classes 🔴

**Definition:**
Classes that cannot be instantiated and require subclasses to implement specific methods.

**Code Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        return f"Shape with area {self.area()}"

# Cannot instantiate
# shape = Shape()  # TypeError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())  # 15
print(rect.description())  # Shape with area 15

# Check if abstract
from abc import ABCMeta
print(isinstance(Shape, ABCMeta))  # True
```

**Key Takeaway:**
Use ABC for interfaces and contracts. Subclasses must implement abstract methods.

---

### Q49. Method Resolution Order (MRO) 🔴

**Definition:**
Order in which Python searches for methods in class hierarchy, especially with multiple inheritance.

**Code Example:**
```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.method()  # B

# View MRO
print(D.mro())
# [D, B, C, A, object]

# C3 Linearization algorithm
print(D.__mro__)

# Diamond problem
class Base:
    def method(self):
        print("Base")

class Left(Base):
    def method(self):
        print("Left")
        super().method()

class Right(Base):
    def method(self):
        print("Right")
        super().method()

class Child(Left, Right):
    def method(self):
        print("Child")
        super().method()

c = Child()
c.method()
# Child -> Left -> Right -> Base
```

**Key Takeaway:**
MRO uses C3 linearization. Check with `.mro()`. Use `super()` for cooperative inheritance.

---

### Q50. Type Hints and Annotations 🔴

**Definition:**
Optional type information for function parameters and return values (Python 3.5+).

**Code Example:**
```python
from typing import List, Dict, Tuple, Optional, Union, Callable

# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# Collections
def process_items(items: List[int]) -> Dict[str, int]:
    return {"count": len(items), "sum": sum(items)}

# Multiple types
def parse_value(value: Union[int, str]) -> int:
    return int(value)

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Tuple
def get_coordinates() -> Tuple[int, int]:
    return (10, 20)

# Callable
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# Type aliases
Vector = List[float]
def scale(vector: Vector, scalar: float) -> Vector:
    return [x * scalar for x in vector]

# Generic types
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Type checking (use mypy)
# mypy script.py
```

**Key Takeaway:**
Type hints improve code readability and enable static type checking. Use `mypy` for verification.

---

### Q52. `__slots__` 🔴

**Definition:**
Explicitly declare instance attributes to reduce memory usage and prevent dynamic attribute creation.

**Code Example:**
```python
# Without __slots__ (uses __dict__)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
print(p1.__dict__)  # {'name': 'Alice', 'age': 25}
p1.email = "alice@example.com"  # Can add new attributes

# With __slots__
class PersonSlots:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = PersonSlots("Bob", 30)
# print(p2.__dict__)  # AttributeError: no __dict__
# p2.email = "bob@example.com"  # AttributeError

# Memory comparison
import sys
print(sys.getsizeof(p1.__dict__))  # ~120 bytes
print(sys.getsizeof(p2))  # ~64 bytes

# __slots__ with inheritance
class Employee(PersonSlots):
    __slots__ = ['employee_id']
    
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.employee_id = emp_id
```

**Key Takeaway:**
Use `__slots__` for memory optimization with many instances. Prevents dynamic attributes.

---

### Q53. Weak References 🔴

**Definition:**
References that don't prevent garbage collection of the referenced object.

**Code Example:**
```python
import weakref
import gc

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"MyClass({self.name})"

# Strong reference
obj = MyClass("test")
print(obj)  # MyClass(test)

# Weak reference
weak = weakref.ref(obj)
print(weak())  # MyClass(test)

# After deleting strong reference
del obj
gc.collect()
print(weak())  # None (object was garbage collected)

# WeakValueDictionary
cache = weakref.WeakValueDictionary()
obj = MyClass("cached")
cache['key'] = obj
print(cache['key'])  # MyClass(cached)

del obj
gc.collect()
print('key' in cache)  # False

# Practical use: caching
class DataManager:
    def __init__(self):
        self.cache = weakref.WeakValueDictionary()
    
    def get_data(self, key):
        if key in self.cache:
            return self.cache[key]
        data = self.load_data(key)  # Expensive operation
        self.cache[key] = data
        return data
    
    def load_data(self, key):
        return MyClass(f"data_{key}")
```

**Key Takeaway:**
Weak references allow garbage collection. Use for caches and breaking circular references.

---

### Q54. Python Optimization 🔴

**Definition:**
Techniques to improve Python code performance.

**Code Example:**
```python
import time

# 1. Use built-ins (faster than loops)
# Slow
result = []
for i in range(1000000):
    result.append(i * 2)

# Fast
result = [i * 2 for i in range(1000000)]

# Fastest
result = list(map(lambda x: x * 2, range(1000000)))

# 2. Use local variables (faster lookup)
import math

# Slow
def calculate_slow():
    result = 0
    for i in range(100000):
        result += math.sqrt(i)
    return result

# Fast (cache in local)
def calculate_fast():
    result = 0
    sqrt = math.sqrt  # Local reference
    for i in range(100000):
        result += sqrt(i)
    return result

# 3. Use generators for large datasets
# Memory intensive
def get_numbers():
    return [i for i in range(1000000)]

# Memory efficient
def get_numbers_gen():
    return (i for i in range(1000000))

# 4. String concatenation
# Slow (creates many intermediate strings)
s = ""
for i in range(10000):
    s += str(i)

# Fast (single allocation)
s = "".join(str(i) for i in range(10000))

# 5. Use sets for membership testing
# Slow (O(n))
items = list(range(10000))
1000 in items

# Fast (O(1))
items = set(range(10000))
1000 in items

# 6. Profile code
import cProfile
cProfile.run('calculate_slow()')

# 7. Use __slots__ for many instances
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**Key Takeaway:**
Use built-ins, list comprehensions, generators, sets, local variables, and profiling for optimization.

---

### Q55. Circular Imports 🔴

**Definition:**
When two or more modules import each other, causing import errors.

**Code Example:**
```python
# module_a.py
from module_b import func_b

def func_a():
    print("Function A")
    func_b()

# module_b.py
from module_a import func_a  # Circular import!

def func_b():
    print("Function B")
    func_a()

# This causes: ImportError

# Solution 1: Restructure code
# shared.py
def func_shared():
    print("Shared")

# module_a.py
from shared import func_shared

# Solution 2: Import inside function
# module_a.py
def func_a():
    from module_b import func_b  # Import when needed
    func_b()

# Solution 3: Import module, not function
# module_a.py
import module_b

def func_a():
    module_b.func_b()

# Solution 4: Reorganize into single module or package
```

**Key Takeaway:**
Avoid circular imports by restructuring, importing inside functions, or importing modules instead of objects.

---

### Q56. Context Variables 🔴

**Definition:**
Thread-safe storage for context-local state (Python 3.7+).

**Code Example:**
```python
from contextvars import ContextVar
import asyncio

# Create context variable
request_id = ContextVar('request_id', default=None)

async def process_request(req_id):
    request_id.set(req_id)
    await task1()
    await task2()

async def task1():
    print(f"Task1 processing request: {request_id.get()}")

async def task2():
    print(f"Task2 processing request: {request_id.get()}")

async def main():
    await asyncio.gather(
        process_request("REQ-001"),
        process_request("REQ-002")
    )

asyncio.run(main())
# Each coroutine sees its own request_id

# Use in web frameworks
user_context = ContextVar('user')

def get_current_user():
    return user_context.get()

def set_current_user(user):
    user_context.set(user)
```

**Key Takeaway:**
Context variables provide async-safe context isolation. Better than thread-local for async code.

---

### Q57. Data Classes 🔴

**Definition:**
Decorator to automatically generate special methods for classes holding data (Python 3.7+).

**Code Example:**
```python
from dataclasses import dataclass, field
from typing import List

# Without dataclass
class PersonOld:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

# With dataclass
@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown"  # Default value

p1 = Person("Alice", 25)
p2 = Person("Alice", 25)
print(p1)  # Person(name='Alice', age=25, email='unknown')
print(p1 == p2)  # True

# Advanced features
@dataclass(frozen=True)  # Immutable
class Point:
    x: int
    y: int

# p = Point(1, 2)
# p.x = 10  # FrozenInstanceError

@dataclass(order=True)  # Enable comparison
class Student:
    name: str
    grade: float = field(compare=True)
    age: int = field(compare=False)

s1 = Student("Alice", 95.0, 20)
s2 = Student("Bob", 90.0, 22)
print(s1 > s2)  # True (compares grade)

# Post-init processing
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)
    
    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(5, 3)
print(r.area)  # 15

# Default factory
@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)

t = Team("Alpha")
t.members.append("Alice")
```

**Key Takeaway:**
Use `@dataclass` for classes that primarily hold data. Auto-generates `__init__`, `__repr__`, `__eq__`.

---

### Q58. f-strings vs format() 🔴

**Definition:**
Different string formatting methods in Python.

**Code Example:**
```python
name = "Alice"
age = 25

# 1. Old style (%)
s1 = "Name: %s, Age: %d" % (name, age)

# 2. str.format()
s2 = "Name: {}, Age: {}".format(name, age)
s3 = "Name: {0}, Age: {1}".format(name, age)
s4 = "Name: {n}, Age: {a}".format(n=name, a=age)

# 3. f-strings (Python 3.6+, fastest)
s5 = f"Name: {name}, Age: {age}"

# Expressions in f-strings
print(f"Next year: {age + 1}")
print(f"Uppercase: {name.upper()}")

# Format specifications
price = 49.99
print(f"Price: ${price:.2f}")  # $49.99
print(f"Hex: {255:x}")  # ff
print(f"Binary: {10:b}")  # 1010

# Alignment
print(f"{'left':<10}|")   # left      |
print(f"{'right':>10}|")  # right|
print(f"{'center':^10}|") #  center  |

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d %H:%M:%S}")

# Debugging (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")  # x=10, y=20

# Performance comparison
import timeit
print(timeit.timeit('f"{name} {age}"', globals=globals()))
print(timeit.timeit('"Name: {}, Age: {}".format(name, age)', globals=globals()))
# f-strings are fastest
```

**Key Takeaway:**
Use f-strings (fastest, most readable). Supports expressions, formatting, and debugging.

---

### Q59. EAFP vs LBYL 🔴

**Definition:**
- **EAFP**: Easier to Ask for Forgiveness than Permission (try-except)
- **LBYL**: Look Before You Leap (if-else checks)

**Code Example:**
```python
# LBYL - Check before action
d = {'key': 'value'}

# LBYL style
if 'key' in d:
    value = d['key']
else:
    value = None

# EAFP - Try and handle exception
try:
    value = d['key']
except KeyError:
    value = None

# File operations
# LBYL
import os
if os.path.exists('file.txt'):
    with open('file.txt', 'r') as f:
        content = f.read()
else:
    content = None

# EAFP (Pythonic)
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = None

# Attribute access
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")

# LBYL
if hasattr(person, 'age'):
    age = person.age
else:
    age = 0

# EAFP (Better for duck typing)
try:
    age = person.age
except AttributeError:
    age = 0

# Or use getattr
age = getattr(person, 'age', 0)

# Performance: EAFP is faster when exceptions are rare
import timeit

d = {'a': 1}

lbyl = """
if 'a' in d:
    x = d['a']
"""

eafp = """
try:
    x = d['a']
except KeyError:
    pass
"""

print(timeit.timeit(lbyl, globals=globals()))  # Slower
print(timeit.timeit(eafp, globals=globals()))  # Faster
```

**Key Takeaway:**
Python prefers EAFP (Pythonic). Use try-except instead of checking conditions. Faster when exceptions are rare.

---

### Q60. Python Design Patterns 🔴

**Definition:**
Common solutions to recurring software design problems.

**Code Example:**
```python
# 1. Singleton
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError(f"Unknown animal: {animal_type}")

# 3. Observer
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")

# 4. Strategy
class SortStrategy:
    def sort(self, data):
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Quick sort logic

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def execute(self, data):
        return self.strategy.sort(data)

# 5. Decorator Pattern
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
print(milk_coffee.cost())  # 7

# 6. Builder
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
    
    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni})"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def build(self):
        return self.pizza

pizza = PizzaBuilder().set_size("large").add_cheese().add_pepperoni().build()
print(pizza)
```

**Key Takeaway:**
Design patterns solve common problems. Know Singleton, Factory, Observer, Strategy, Decorator, Builder for interviews.

---


---

## 📊 Key Comparison Tables

### Data Types Comparison

| Type | Mutable | Ordered | Duplicates | Syntax | Use Case |
|------|---------|---------|------------|--------|----------|
| **List** | Yes | Yes | Yes | `[1,2,3]` | Dynamic collections |
| **Tuple** | No | Yes | Yes | `(1,2,3)` | Fixed data, dict keys |
| **Set** | Yes | No | No | `{1,2,3}` | Unique items, fast lookup |
| **Dict** | Yes | Yes (3.7+) | Keys: No | `{'a':1}` | Key-value pairs |
| **String** | No | Yes | Yes | `"abc"` | Text data |

### Memory and Performance

| Operation | List | Tuple | Set | Dict |
|-----------|------|-------|-----|------|
| **Access by index** | O(1) | O(1) | N/A | N/A |
| **Search** | O(n) | O(n) | O(1) | O(1) |
| **Insert/Delete** | O(n) | N/A | O(1) | O(1) |
| **Memory** | High | Low | Medium | High |

### Python 2 vs Python 3

| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| **Print** | `print "hello"` | `print("hello")` |
| **Division** | `5/2 = 2` | `5/2 = 2.5` |
| **Unicode** | ASCII default | Unicode default |
| **range()** | Returns list | Returns iterator |
| **input()** | Returns string | Returns string (eval removed) |

---

## 🎯 Top 15 Most Asked Questions

1. **🟢 List vs Tuple** - Most common data structure question
2. **🟢 Mutable vs Immutable** - Fundamental concept
3. **🟡 Decorators** - Advanced but very popular
4. **🟡 Generators and Yield** - Memory efficiency
5. **🟢 *args and **kwargs** - Function parameters
6. **🟡 GIL (Global Interpreter Lock)** - Concurrency
7. **🟢 Exception Handling** - Error management
8. **🟡 List Comprehension** - Pythonic code
9. **🟢 Lambda Functions** - Functional programming
10. **🟡 Shallow vs Deep Copy** - Object copying
11. **🟡 Multithreading vs Multiprocessing** - Concurrency
12. **🟢 `is` vs `==`** - Identity vs equality
13. **🟡 Context Managers** - Resource management
14. **🟡 Map, Filter, Reduce** - Functional tools
15. **🔴 Metaclasses** - Advanced OOP

---

## 📝 Python Syntax Cheat Sheet

### Common Patterns
```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}

# Lambda functions
add = lambda x, y: x + y
sorted_list = sorted(data, key=lambda x: x['age'])

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce
total = reduce(lambda x, y: x + y, numbers)

# Context managers
with open('file.txt', 'r') as f:
    content = f.read()

# Multiple assignment
a, b = 10, 20
a, b = b, a  # Swap

# Unpacking
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]

# Enumerate
for idx, val in enumerate(['a', 'b', 'c']):
    print(idx, val)

# Zip
for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)
```

---

## 💡 Interview Tips

### Preparation Strategy
- **Week 1**: Basics (Q1-Q20) + Practice coding
- **Week 2**: Intermediate (Q21-Q35) + OOP concepts
- **Week 3**: Advanced (Q36-Q50) + Design patterns
- **Week 4**: Real projects + Mock interviews

### Common Mistakes to Avoid
❌ Not understanding mutability (list default arguments)
❌ Confusing `is` and `==`
❌ Not using list comprehensions (writing verbose loops)
❌ Ignoring exception handling
❌ Not knowing when to use generators

### Interview Success Tips
✅ Write Pythonic code (use idioms)
✅ Explain time and space complexity
✅ Handle edge cases
✅ Use appropriate data structures
✅ Know standard library modules

---

[⬆️ Back to Table of Contents](#-table-of-contents)

**Good luck with your Python interviews! 🐍🚀**
