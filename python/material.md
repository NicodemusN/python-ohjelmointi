# ---

# marp: true

# theme: latexlike

# paginate: true

# ---

# Introduction to Python Programming

## 🧑‍💻 Jussi Pohjolainen, TAMK

---

## Welcome!

- No previous coding experience needed!
- Today you'll learn:
  - What Python is
  - How to write simple programs
  - Key concepts: variables, data types, control flow, functions, input/output, and collections

---

## What is Python?

- Python is a **popular, easy-to-read** programming language.
- Used in:
  - Web development
  - Data science
  - AI & machine learning
  - Automation
- Python code looks like "plain" English compared to other languages

---

## Your First Python Program

```python
print("Hello, world!")
```

- `print()` shows text on the screen
- Strings are inside quotes `"..."`
- Run your app
  - Open VS Code
  - Create new file `code.py`
  - Save file to some directory
  - Open command prompt and go the directory: `cd <path to your dir>`
  - Run your app `python code.py`

---

## ️ The `print()` Function

```python
print("Hello", "world")
print("Age:", 25)
print("Sum:", 2 + 3)
```

### Advanced print options:

```python
print("A", "B", "C", sep="-")  # A-B-C
print("No newline", end="...")
print("Continued")
```

---

## Types

| **Category**         | **Type**    | **Description**                              | **Example**                | **Value or Reference** |
| -------------------- | ----------- | -------------------------------------------- | -------------------------- | ---------------------- |
| **Basic Data Types** | `int`       | Integer numbers                              | `x = 42`                   | Value (immutable)      |
|                      | `float`     | Floating-point numbers                       | `x = 3.14`                 | Value (immutable)      |
|                      | `bool`      | Boolean values                               | `x = True`                 | Value (immutable)      |
|                      | `str`       | Text strings                                 | `x = "hello"`              | Value (immutable)      |
| **Sequence Types**   | `list`      | Mutable ordered collection                   | `x = [1, 2, 3]`            | Reference (mutable)    |
|                      | `tuple`     | Immutable ordered collection                 | `x = (1, 2, 3)`            | Value (immutable)      |
|                      | `range`     | Sequence of numbers                          | `x = range(5)`             | Value (immutable)      |
| **Set Types**        | `set`       | Mutable unordered collection of unique items | `x = {1, 2, 3}`            | Reference (mutable)    |
|                      | `frozenset` | Immutable version of a set                   | `x = frozenset([1, 2, 3])` | Value (immutable)      |
| **Mapping Type**     | `dict`      | Key-value mapping                            | `x = {"a": 1, "b": 2}`     | Reference (mutable)    |

---

## Value Types

- Hold the actual **value**
- Changing one **does not affect** the other
- Examples: `int`, `float`, `bool`, `str`, `tuple`

```python
x = 10
y = x      # Copy value
x = 20
print(y)   # ➜ 10 (unchanged)
```

---

## Reference Types

- Hold a reference (memory address) to the value
- Changing one affects the other
- Examples: list, dict, set

```python
a = [1, 2, 3]
b = a       # Copy reference
a.append(4)
print(b)    # ➜ [1, 2, 3, 4] (changed)
```

---

## Visual Summary

```text
# Value Type
x = 10
y = x
x = 20

   x     y
   ↓     ↓
  20    10

# Reference Type
a = [1, 2]
b = a
a.append(3)

   a, b
    ↓
  [1, 2, 3]
```

---

## Rule of Thumb

| **Type** | **Value / Reference** | **Mutable?** |
| -------- | --------------------- | ------------ |
| `int`    | Value Type            | ❌           |
| `float`  | Value Type            | ❌           |
| `str`    | Value Type            | ❌           |
| `tuple`  | Value Type            | ❌           |
| `list`   | Reference Type        | ✅           |
| `dict`   | Reference Type        | ✅           |
| `set`    | Reference Type        | ✅           |

---

## Variables and `type()`

```python
name = "Alice"
age = 30
is_admin = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(is_admin))  # <class 'bool'>
```

---

## Strings in Python

### String literals:

```python
a = 'single quotes'
b = "double quotes"
c = '''triple quotes for
          multi-line
       strings'''
```

### Access characters and length:

```python
text = "Python"
print(text[0])       # 'P'
print(len(text))     # 6
```

### Formatted strings (f-strings):

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

---

## User Input with `input()`

- The `input()` function is used to read user input from the command line. It always returns the user input as a string, even if the input looks like a number.

```python
variable = input("Prompt message: ")
```

- The "Prompt message" is optional and will be shown before waiting for user input.
- Note: `input()` always returns a string:

```python
age = input("How old are you? ")
print(type(age))  # Always <class 'str'>, even if you type "25"
```

- Another example:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

- Common error:

```python
# This will cause an error if input is not a number
number = int(input("Enter a number: "))
```

- To avoid errors, always validate user input if needed:

```python
user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    print("You entered:", number)
else:
    print("That's not a valid number.")
```

---

## Type Casting: Examples

```python
x = "5"
y = int(x) + 10
print(y)  # 15

a = float("3.14")
b = str(42)
c = bool("non-empty")
```

And proper usage with exception handling:

```python
try:
    x = int(input("give integer: "))
    y = int(input("give integer: "))
    print(x / y)
except ValueError:
    print("error: give integers")
except ZeroDivisionError:
    print("error: Do not divide with zero.")
```

---

## Memory Address: `id()`

```python
x = 100
# Returns the identity of the object, which
# corresponds to its memory address (in CPython implementation)

# outputs something like 4348259584
print(id(x))

# outputs something like 0x10328ed00
# Developers from C/C++/Java backgrounds are used to seeing
# memory addresses in hex (0x7ffeefbff5c0), not huge base-10 integers.
print(hex(id(x)))
```

---

## Control Flow: `if`, `elif`, `else`

Control flow allows your program to **make decisions**. In Python, you use `if`, `elif` (else if), and `else` to run different blocks of code based on conditions.

---

### Basic Structure

```python
if condition1:
    # Run this block if condition1 is True
elif condition2:
    # Run this block if condition1 is False AND condition2 is True
else:
    # Run this block if all above conditions are False
```

- Each condition must be an **expression that evaluates to True or False**.
- Use **indentation** (typically 4 spaces) instead of `{}`.
- You can have **zero or many `elif`**, but only **one `else`** at the end.

---

### Simple Example

```python
temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("Nice weather.")
else:
    print("It's a bit chilly.")
```

Output:

```
Nice weather.
```

- Note: `elif` and `else` are here optional!

---

## Comparison Operators

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `x == 5` |
| `!=`     | Not equal to     | `x != 5` |
| `>`      | Greater than     | `x > 5`  |
| `<`      | Less than        | `x < 5`  |
| `>=`     | Greater or equal | `x >= 5` |
| `<=`     | Less or equal    | `x <= 5` |

---

## Multiple Conditions with Logic Operators

```python
x = 10

if x > 5 and x < 20:
    print("x is between 5 and 20")
```

```python
y = 15

if y < 10 or y > 12:
    print("y is outside 10-12 range")
```

```python
logged_in = True

if not logged_in:
    print("Please log in.")
```

### Python vs Java:

| Python Expression    | Java Equivalent                     | Meaning                                |
| -------------------- | ----------------------------------- | -------------------------------------- |
| `9 <= hour <= 17`    | `hour >= 9 && hour <= 17`           | `hour` is between 9 and 17 (inclusive) |
| `1 < x < 10`         | `x > 1 && x < 10`                   | `x` is greater than 1 and less than 10 |
| `a == b == c`        | `a == b && b == c`                  | All three variables are equal          |
| `x != y != z`        | `x != y && y != z`                  | `x`, `y`, and `z` are all different    |
| `not (x == y)`       | `!(x == y)`                         | `x` is not equal to `y`                |
| `x in [1, 2, 3]`     | `Arrays.asList(1,2,3).contains(x)`  | `x` is in the list                     |
| `x not in [1, 2, 3]` | `!Arrays.asList(1,2,3).contains(x)` | `x` is not in the list                 |
| `if x:`              | `if (x != 0)` or `if (x != null)`   | Truthy check                           |

---

## Nested `if` Statements

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry allowed.")
    else:
        print("Ticket required.")
else:
    print("You must be 18 or older.")
```

---

## Summary of control structures

- Use `if` to check a condition.
- Use `elif` for extra conditions.
- Use `else` as a fallback.
- Combine with `and`, `or`, `not` for more complex logic.
- Indentation is critical!

---

## Python Loops: `while` and `for`

Loops allow you to **repeat blocks of code**. Python supports two main types:

- `while` loop: Repeats while a condition is `True`
- `for` loop: Iterates over items in a sequence like a list or range

---

### `while` Loop – Repeat While Condition is True

#### Syntax

```python
while condition:
    # code block
```

- The condition is checked **before** each iteration.
- If the condition becomes `False`, the loop stops.
- Make sure the loop has an **exit condition**, or it will run forever.

---

#### Example 1: Count to 4

```python
i = 1
while i <= 4:
    print(i)
    i += 1
```

Output:

```
1
2
3
4
```

---

#### Example 2: Infinite Loop (️)

```python
while True:
    print("This goes on forever!")
```

Press Ctrl+C to stop it in terminal.

---

#### Using `break` in `while`

```python
x = 0
while True:
    print(x)
    x += 1
    if x > 5:
        break
```

---

### Using `continue` in `while`

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

Output:

```
1
2
4
5
```

---

### Avoid Break and Continue?

| Issue                      | Explanation                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| ❌ Hidden logic            | Using `break` or `continue` deep inside a loop body can hide exit/skip logic and hurt readability.                   |
| ❌ Hard to trace           | If the loop is long or nested, jumping in/out makes debugging more difficult.                                        |
| ❌ Overuse                 | Relying on these for all logic can lead to “spaghetti code”.                                                         |
| ❌ Control structure abuse | Using `break`/`continue` when better structured conditions (like `if`, flags, or helper functions) would be clearer. |

---

### `for` Loop - Iterate Over Items

#### Syntax

```python
for item in iterable:
    # code block
```

- Loops over each iterables:
  - `str`, `range`, `list`, `tuple` ,`dict` ,`set` ,`emumerate` and others.
  - These all _are iterables_.
- You don't need an index unless you want one explicitly, use `enumerate` for this. (See later in material)

---

#### Example 1: Loop Over List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

---

#### Example 2: Loop Over String

```python
for char in "Python":
    print(char)
```

---

#### Example 3: Using `range()`

```python
for i in range(3):
    print(i)
```

Output:

```
0
1
2
```

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

#### Common Python Examples

```python
# loop over range
for i in range(1, 6):
    print(i)

# loop over list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index:
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

#### Using `break` in `for`

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

---

#### Using `continue` in `for`

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

---

### Summary

| Feature    | `while` Loop              | `for` Loop                       |
| ---------- | ------------------------- | -------------------------------- |
| Best for   | Unknown number of repeats | Known number or iterable         |
| Condition  | Checked before each loop  | Loops over sequence or range     |
| Common use | Waiting for user input    | Iterating lists, strings, ranges |

Both loop types support `break` (stop loop) and `continue` (skip current iteration).

---

### `break` and `continue`

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## Collections Overview

### Lists

- A **list** is like a dynamic array – it can grow or shrink.
- Elements are ordered and mutable (can be changed).
- Indexing starts from `0`.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")      # Add new item
print(fruits[0])             # Access first item
fruits[1] = "blueberry"      # Modify an item
print(fruits)                # ['apple', 'blueberry', 'cherry', 'orange']
```

#### Useful Methods with Examples:

```python
numbers = [3, 1, 4, 1, 5]

numbers.append(9)            # [3, 1, 4, 1, 5, 9]
numbers.remove(1)            # Removes first 1 → [3, 4, 1, 5, 9]
numbers.sort()               # [1, 3, 4, 5, 9]
total = sum(numbers)         # 22
length = len(numbers)        # 5
print(numbers[2])            # 4
print(3 in numbers)          # True
```

---

### Tuples

- A **tuple** is like a list, but **immutable** – cannot be changed after creation.
- Used for fixed data structures (e.g., coordinates, settings).
- Supports unpacking.

```python
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# point[0] = 100  # ❌ Error: Tuples can't be changed
```

#### Operations with Examples:

```python
coords = (1, 2, 3)
print(coords[1])             # 2

a, b, c = coords             # unpacking
print(a, b, c)               # 1 2 3
```

---

### Sets

- A **set** is an unordered collection of unique items.
- Automatically removes duplicates.
- Fast membership testing.

```python
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)        # {1, 2, 3}
unique_numbers.add(4)
print(3 in unique_numbers)   # True
```

#### Operations with Examples:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)                     # {1, 2, 3, 6}
a.remove(2)                  # {1, 3, 6}
a.discard(10)                # Safe removal (no error)

union = a | b                # {1, 3, 4, 5, 6}
intersection = a & b         # {3}
difference = a - b           # {1, 6}
```

---

### Dictionaries

- A **dictionary** stores data as key-value pairs.
- Keys must be unique and immutable (usually strings or numbers).

```python
person = {"name": "Alice", "age": 30}
print(person["name"])        # Alice
person["age"] = 31           # Update value
person["job"] = "Engineer"   # Add new key-value pair
print(person)
```

#### Useful Methods and Syntax with Examples:

```python
person = {"name": "Bob", "city": "Paris"}

print(person["city"])        # Paris
print(person.get("age"))     # None

person["age"] = 45
print(person.items())        # dict_items([('name', 'Bob'), ('city', 'Paris'), ('age', 45)])
print(person.keys())         # dict_keys(['name', 'city', 'age'])
print(person.values())       # dict_values(['Bob', 'Paris', 45])
```

---

### Summary Table

| Type       | Ordered | Mutable | Duplicates | Syntax          | Example             |
| ---------- | ------- | ------- | ---------- | --------------- | ------------------- |
| List       | ✅      | ✅      | ✅         | `[]`            | `["a", "b", "c"]`   |
| Tuple      | ✅      | ❌      | ✅         | `()`            | `("x", "y")`        |
| Set        | ❌      | ✅      | ❌         | `{}` or `set()` | `{1, 2, 3}`         |
| Dictionary | ❌      | ✅      | Keys: ❌   | `{key: value}`  | `{"name": "Alice"}` |

---

## Functions

### What is a Function?

- A **function** is a reusable block of code that performs a specific task.
- Functions help you avoid repeating code and make your programs easier to read and maintain.

---

### Why Use Functions?

- **Reusability**: Write once, use many times.
- **Organization**: Break large problems into smaller parts.
- **Readability**: Code becomes easier to understand.
- **Debugging**: Easier to test and fix issues in isolated blocks.

---

#### Defining a Function

- Use the `def` keyword followed by the function name and parentheses.
- Example:

```python
def greet():
    print("Hello, world!")
```

---

#### Calling a Function

- You run (or "call") a function by using its name followed by parentheses:

```python
greet()  # Output: Hello, world!
```

---

#### Function with Parameters

- Parameters allow you to pass information into a function:

```python
def greet(name):
    print(f"Hello, {name}!")
```

```python
greet("Alice")  # Output: Hello, Alice!
```

---

#### Function with Return Value

- Functions can **return** results using the `return` keyword:

```python
def add(a, b):
    return a + b
```

```python
result = add(2, 3)
print(result)  # Output: 5
```

---

#### Default Parameters

- You can give default values to parameters:

```python
def greet(name="stranger"):
    print(f"Hello, {name}!")
```

```python
greet()         # Output: Hello, stranger!
greet("Alice")  # Output: Hello, Alice!
```

---

#### Keyword Arguments

- You can name arguments when calling the function:

```python
def subtract(a, b):
    return a - b

print(subtract(b=5, a=10))  # Output: 5
```

---

#### Summary

- Functions = named blocks of code.
- Use `def` to define, `()` to call.
- Can have parameters and return values.
- Help make your code DRY (Don't Repeat Yourself).

---
