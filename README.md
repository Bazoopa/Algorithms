# Algorithms
Algorithm training

# Useful Python Poetry Commands

Setup a new project:
 - poetry new poetry-demo

initialise pre-existing project (super useful):
 - poetry init

install dependencies:
 - poetry install

Add dependency:
 - poetry add <package name>


# Useful builtin Python functions:

https://docs.python.org/3/library/functions.html

# Useful builtin Python functions

Python provides a rich set of built-in functions that are commonly used for various operations. Here are some of the most frequently used built-in functions categorized by their functionality:

## Basic Functions

- **`print()`**
  - Outputs data to the console.

- **`len()`**
  - Returns the length of an iterable (e.g., list, tuple).

- **`type()`**
  - Returns the type of an object.

- **`zip()`**
  - Aggregates elements from two or more iterables.

- **`map()`**
  - Applies a function to all items in an iterable.

- **`split()`**
  - Splits a string into a list of substrings based on a delimiter.

- **`sum()`**
  - Sums the items of an iterable.

## Conversion Functions

- **`int()`**
  - Converts a value to an integer.

- **`float()`**
  - Converts a value to a floating-point number.

- **`str()`**
  - Converts a value to a string.

- **`list()`**
  - Converts an iterable to a list.

- **`dict()`**
  - Creates a dictionary.

## Iteration and Filtering

- **`range()`**
  - Generates a sequence of numbers.

- **`enumerate()`**
  - Adds a counter to an iterable.

- **`filter()`**
  - Constructs an iterator from elements of an iterable for which a function returns true.

## Aggregation and Comparison

- **`sum()`**
  - Sums the items of an iterable.

- **`min()`**
  - Returns the smallest item in an iterable or among arguments.

- **`max()`**
  - Returns the largest item in an iterable or among arguments.

## Data Handling

- **`open()`**
  - Opens a file and returns a corresponding file object.

- **`input()`**
  - Reads a line from input, usually from the user.

## Object and Attribute Handling

- **`isinstance()`**
  - Checks if an object is an instance or subclass of a class or tuple of classes.

- **`hasattr()`**
  - Checks if an object has a specific attribute.

- **`getattr()`**
  - Returns the value of a named attribute of an object.

## Miscellaneous

- **`sorted()`**
  - Returns a sorted list of the specified iterable.

- **`reversed()`**
  - Returns a reversed iterator.

---

## Lambda Functions

Lambda functions, also known as anonymous functions, are small, single-expression functions that can have any number of arguments but only one expression. They are defined using the `lambda` keyword. Lambda functions are particularly useful when you need a simple function for a short period of time, often as an argument to higher-order functions (like `map()`, `filter()`, etc.).

---

# Useful Built-in String Methods

Python provides several built-in string methods that are essential for manipulating and processing strings effectively.

## Conversion and Case Manipulation

- **`str.upper()`**
  - Converts all characters in a string to uppercase.
  
- **`str.lower()`**
  - Converts all characters in a string to lowercase.
  
- **`str.capitalize()`**
  - Converts the first character of a string to uppercase and the rest to lowercase.
  
- **`str.title()`**
  - Converts the first character of each word to uppercase and the rest to lowercase.

## Whitespace Removal

- **`str.strip()`**
  - Removes leading and trailing whitespace (spaces, tabs, newlines).
  
- **`str.lstrip()`**
  - Removes leading whitespace (spaces, tabs, newlines).
  
- **`str.rstrip()`**
  - Removes trailing whitespace (spaces, tabs, newlines).

## Search and Replace

- **`str.find(substring)`**
  - Returns the lowest index where `substring` is found in the string (-1 if not found).
  
- **`str.replace(old, new)`**
  - Returns a new string where all occurrences of `old` are replaced by `new`.
  
- **`str.startswith(prefix)`**
  - Returns `True` if the string starts with the specified `prefix`; otherwise, returns `False`.
  
- **`str.endswith(suffix)`**
  - Returns `True` if the string ends with the specified `suffix`; otherwise, returns `False`.

## Splitting and Joining

- **`str.split(sep)`**
  - Splits the string into a list of substrings using `sep` as the delimiter.
  
- **`str.join(iterable)`**
  - Concatenates elements of an iterable (such as a list) into a single string, with `str` as the separator.

## Checking and Formatting

- **`str.isalnum()`**
  - Returns `True` if all characters in the string are alphanumeric (letters or numbers); otherwise, returns `False`.
  
- **`str.isdigit()`**
  - Returns `True` if all characters in the string are digits; otherwise, returns `False`.
  
- **`str.isalpha()`**
  - Returns `True` if all characters in the string are alphabetic (letters); otherwise, returns `False`.
  
- **`str.islower()`**
  - Returns `True` if all characters in the string are lowercase; otherwise, returns `False`.
  
- **`str.isupper()`**
  - Returns `True` if all characters in the string are uppercase; otherwise, returns `False`.
  
- **`str.format()`**
  - Formats the string according to the format specifier.

## Other Useful Methods

- **`str.count(substring)`**
  - Returns the number of occurrences of `substring` in the string.
  
- **`str.index(substring)`**
  - Returns the lowest index where `substring` is found in the string (raises ValueError if not found).

These methods are crucial for various string operations in Python programming and are extensively used in data processing, text manipulation, and more.

---

# Python Naming Standards

- **``**


Python follows a set of conventions for naming variables, functions, classes, and other entities in order to promote readability and consistency across codebases. These guidelines are detailed in PEP 8, the Style Guide for Python Code.

## Variables and Function Names
- **`Variables: Use lowercase words separated by underscores (snake_case).`**

```python
user_name = "John Doe"
max_attempts = 5
total_sum = 100.0
```

- **`Functions: Use lowercase words separated by underscores (snake_case). Use descriptive names that convey the function's purpose.`**

```python
def calculate_total_price(item_prices):
    pass

def validate_input(user_input):
    pass
```

## Constants

- **`Constants: Are usually defined at the module level and written in uppercase letters with underscores separating words (CAPITALIZED_WITH_UNDERSCORES).`**

```python
MAX_RETRIES = 5
PI = 3.14159
```

## Classes and Exceptions

- **`Classes: Use CapWords convention (also known as PascalCase), where each word starts with a capital letter and no underscores.`**

```python
class MyClass:
    pass
```

- **`Exceptions: Use the suffix "Error" for exception classes.`**

```python
class MyCustomError(Exception):
    pass
```

## Global and Local Variables

- **`Global Variables: Should be used sparingly, and follow the same conventions as regular variables.`**

- **`Local Variables: Follow the same conventions as regular variables.`**

## Function Arguments

- **`Function arguments should follow the same naming conventions as variables.`**

## Private Variables and Methods

- **`Use a leading underscore (_) to indicate that a variable or method is intended for internal use only.`**

```python
class MyClass:
    def __init__(self):
        self._internal_data = []
    
    def _process_data(self):
        pass
```

## Abbreviations and Acronyms

- **`Treat acronyms and abbreviations as words in names, using consistent capitalization.`**

```python
xml_parser = XmlParser()
num_http_requests = 100
```

---





