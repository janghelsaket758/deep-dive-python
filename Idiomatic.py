# Shebang statement for scripts
# This line is used to indicate the script's interpreter
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Zen of Python, by Tim Peters
import this

# One statement per line, the idiomatic way
# This is the preferred style in Python, as it enhances readability
print("Hello")
print("World")

# ALso possible to put to statements in one line,
# use semicolons, but not recommended
print("Hello"); print("World")

true_value = "aaa" # Truthy, or 1, or "ddd", or [1, etc.]
false_value = [] # Falsy, or 0, or "", or None
none_value = None


# Bad  
if true_value == True:
    print("Truthy")

if false_value == False:
    print("Falsy")


# Good
if true_value:
    print("Truthy") 

if not false_value:
    print("Falsy")


# Testing for None
# Using 'is' for identity checks
# This is the preferred way to check for None
if none_value is None: # Instead of none_value == None
    print("None")


# Using 'is not' for identity checks
# This is the preferred way to check for non-None values
if none_value is not None: # Instead of none_value != None
    print("Not None")

# Continuing later with more idiomatic practices...