# ACIT 1515 - Python Exam Study Guide

The following is a *non-exhaustive* set of content reviewing over a number of things we’ve learned so far in the course, as well as a few things we didn’t explicitly cover in lecture but did cover in our notes.

## Variables, types, and input/output

Variables store values under a name. Python is case-sensitive, so `age` and `Age` are different variables. Names cannot start with a number or use a Python keyword.

The main types to know are:

- `str`: text, such as `"Bcit"`
- `int`: whole numbers, such as `12`
- `float`: decimal numbers, such as `12.5`
- `bool`: `True` or `False`
- `None`: represents no value

`input()` always returns a string, even when the user enters a number. Convert it before doing math.

``` python
name = input("Name: ")
age = int(input("Age: "))
print(f"{name} is {age} years old")
```

Use `str()`, `int()`, `float()`, and `bool()` to convert values. Use `type()` to check a value’s type.

```txt
"2" + "3"     # "23"
 2  +  3      # 5
"2" +  3      # TypeError
```

**Operators**

- Math: `+`, , , `/`, `*` for powers, `%` for remainders
- Assignment: `=`, `+=`, `=`, `=`, `/=`
- Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Membership: `in`, `not in`
- Logic: `and`, `or`, `not`

Remember: **`=` assigns a value. `==` checks whether values are equal.**

``` python
x += 1        # same as x = x + 1
7 % 2         # 1
2 ** 3        # 8
```

## Conditional statements

Conditions let you choose which code runs.

``` python
score = 84

if score >= 80:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

An `if`/`elif`/`else` chain runs the first matching branch and skips the rest. Separate `if` statements are checked independently.

My suggestion is to start with `if`, add any needed `elif` branches, and put `else` last. `else` does not take a condition.

Don’t forget: Colons and indentation matter. Code indented under a condition belongs to that condition.

When combining conditions:

- `and`: both conditions must be true
- `or` : at least one must be true
- `not`: reverses whether a condition is true or false

```python
if age >= 18 and has_ticket:
    print("Enter")
```

**Loops**

Use a `while` loop when you want to repeat something while a condition remains true.

```python
counter = 3

while counter > 0:
    print(counter)
    counter -= 1

# prints 3, 2, 1 on separate lines
```

The condition is checked before each iteration, so a `while` loop might never run. Make sure it can eventually stop! (In other words, avoid infinite loops)

Use a `for` loop to go through *values* one at a time.

``` python
cities = ["Vancouver", "Burnaby", "Surrey"]

for city in cities:
    print(city)
```

As we saw during class, you can use `enumerate()` when you need both the index and the value.

``` python
for index, city in enumerate(cities):
    print(index, city)

# 0 Vancouver
# 1 Burnaby
# 2 Surrey
```

`range(start, stop, step)` generates numbers. **The stop value is never included.**

``` python
range(4)          # 0, 1, 2, 3
range(1, 5)       # 1, 2, 3, 4
range(2, 7, 2)    # 2, 4, 6
range(3, 0, -1)   # 3, 2, 1
```

Two loop keywords to remember:

- `break` exits the nearest enclosing loop.
- `continue` skips the rest of the current iteration and moves to the next one.

With nested loops, the inner loop runs inside each iteration of the outer loop. A `break` inside the inner loop only exits that inner loop.

## Strings, lists, and tuples

All three are ordered sequences:

``` python
word = "Python"          # string
letters = ["a", "b"]     # list
letters = ("a", "b")     # tuple
```

Lists are mutable, meaning you can change their elements. Strings and tuples are immutable.

Sequences support indexing, slicing, membership checks, `len()`, `.count()`, and `.index()`.

``` jsx
word = "Python"

word[0]           # "P" — first index is 0
word[-1]          # "n" — last character
word[1:4]         # "yth" — stop index is excluded
word[:2]          # "Py"
word[2:]          # "thon"

len(word)         # 6
"yth" in word     # True
word.count("o")   # 1
word.index("t")   # 2 — first matching position
```

An invalid index raises `IndexError`. Calling `.index()` for a value that is not present raises `ValueError`.

Note: If you’re feeling a bit confused about the difference between `len()` and `.count()` (since we didn’t talk much about `count` in class), see the example code below:

``` python
numbers = [1, 2, 3, 2, 4, 2]

# len() gives the total number of items
print(len(numbers))  
# Output: 6

# .count() looks for a specific item (e.g., how many 2s?)
print(numbers.count(2))  
# Output: 3
```

For lists, you can replace an element or add one to the end:

``` python
letters = ["a", "b"]
letters[0] = "A"
letters.append("c")

# letters is now ["A", "b", "c"]
```

For nested lists, use one index for each level:

``` python
nested = ["a", ["b", "c"]]
nested[1][0]              # "b"
```

You can also convert between sequence types:

``` python
list("abc")              # ["a", "b", "c"]
tuple([1, 2])            # (1, 2)
str([1, 2])              # "[1, 2]"
```

Notice that `str()` keeps the list’s brackets in the resulting text.

## Dictionaries

A dictionary stores key/value pairs. You use a key to access a value.

``` python
dog = {"name": "Charlie", "age": 12}

dog["name"]                # "Charlie"
dog["name"] = "Tater"       # update a value
dog["breed"] = "Ridgeback"  # add a new key/value pair
del dog["age"]             # delete a pair
```

Keys are unique and must be hashable. Strings and numbers work as keys; lists do not. Values can be any type.

Reading or deleting a missing key raises `KeyError`. Assigning a missing key adds it.

``` python
"name" in dog               # checks keys
"Tater" in dog.values()     # checks values
len(dog)                    # number of pairs
```

Dictionary methods:

- `.keys()` gives a view of the keys.
- `.values()` gives a view of the values.
- `.items()` gives a view of `(key, value)` tuples.
- `list(dog.items())` converts the items view to a list.

``` python
for key in dog:
    print(key)

for key, value in dog.items():
    print(key, value)
```

## Functions

Functions group code so you can call it when needed.

``` python
def add(a, b=0):
    total = a + b
    return total

result = add(3, 4)     # 7
add(3)                # 3, using the default b=0
add(b=4, a=3)         # 7, using keyword arguments
```

Terms to know:

- **Parameters** are the names in the function definition: `a` and `b`.
- **Arguments** are the values supplied in a call: `3` and `4`.
- **Default values** are used when an argument is left out.
- **Keyword arguments** identify the parameter by name.

Defining a function does not run its body. You must call it using `()`.

`return` ends the function immediately and sends a value back to the caller. A function without an explicit return value returns `None`.

> As a bottom line rule of thumb, I suggest thinking of it this way:
> 
> **`print()` displays something; `return` gives something back.**

Parameters and variables assigned inside a function are normally local to that function. Trying to use those local names outside it raises `NameError`.

Missing required arguments raises `TypeError`.

## Errors and debugging

There are three main kinds of errors:

- **Syntax error:** the code breaks Python’s rules, such as a missing quote or colon. The file cannot run.
- **Runtime error:** the code starts running, but an operation fails.
- **Logical error:** the code runs, but the result is wrong.

Common runtime errors:

- `TypeError`: incompatible types or incorrect function arguments
- `ValueError`: an invalid value, such as `int("hello")`
- `NameError`: a name has not been defined
- `IndexError`: a sequence index is out of range
- `KeyError`: a dictionary key is missing

Use `try`/`except` to handle an expected error:

``` python
try:
    age = int(input("Age: "))
    print(f"Next year: {age + 1}")
except ValueError:
    print("Enter a whole number.")
```

If an error occurs in `try`, Python skips the rest of that block and runs the matching handler.

For debugging, read the error message and line number, then use `print()` and `type()` to inspect the values involved.

Two string methods from the notes:

``` python
"index.html".endswith(".html")   # True
"123".isnumeric()                # True
```

`.isnumeric()` returns false for `"-3"` and `"3.5"`. It also does not guarantee that every string it accepts can be converted with `int()`.

## Pathlib

`Path` represents a location in the filesystem. Creating a `Path` object does not create a file or folder.

``` python
from pathlib import Path

folder = Path("project")
folder.mkdir()                       # create the folder

file = folder.joinpath("notes.txt")
file.touch()                         # create file if absent
```

- `joinpath()` builds a path to something inside another location.
- `mkdir()` creates a directory.
- `touch()` creates a file if it does not already exist.

## Terminal basics

Run these at the operating system prompt:

``` python
python3 script.py    # run a Python file
python3              # open the Python REPL
pwd                  # show current directory
ls                   # list directory contents
cd folder            # enter a folder
cd ..                # go up one folder
mkdir folder         # create a folder
mv old new           # move or rename
```

The Python REPL uses the `>>>` prompt and accepts Python code. Type `exit()` to leave it.

`PATH` is the list of folders the operating system searches when looking for a command.

## Friendly reminders of things to make sure you understand prior to the midterm:

Try to trace short programs by hand. Pay particular attention to:

- Indentation and which block a line belongs to
- The value of a variable after each loop iteration
- Values being excluded from ranges and slices
- Indexes starting at zero
- Dictionary keys versus sequence indexes
- String input needing conversion before math
- `print()` versus `return`
- The difference between changing a list and trying to change a string or tuple
