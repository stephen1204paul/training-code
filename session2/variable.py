# VARIABLES AND DATA TYPES IN PYTHON
# This file introduces basic Python data types and how variables work

# PYTHON DATA TYPES
# Variables don't need type declarations - Python figures out the type automatically

# String: Text enclosed in quotes
hello_message = "Hello Cloud"

# Integer: Whole numbers
int_message = 100

# Float: Numbers with decimal points
float_message = 100.0

# Boolean: True or False values
bool_message = True

# List: Ordered collection of items (mutable - can be changed)
list_message = [1, 2, 3, 4, 5]

# Tuple: Ordered collection of items (immutable - cannot be changed)
tuple_message = (1, 2, 3, 4, 5)

# Dictionary: Key-value pairs (like a lookup table)
dict_message = {"a": 1, "b": 2, "c": 3}

# EXAMPLE 1: Variables can be updated (accumulator pattern)
# Tracking cumulative time to prepare burgers
time_taken_to_prepare_three_burgers = 0
print(time_taken_to_prepare_three_burgers)  # Output: 0

time_taken_to_prepare_three_burgers += 20  # Time to prepare first burger
print(time_taken_to_prepare_three_burgers)  # Output: 20

time_taken_to_prepare_three_burgers += 10  # Time to prepare second burger
print(time_taken_to_prepare_three_burgers)  # Output: 30

time_taken_to_prepare_three_burgers += 15  # Time to prepare third burger
print(time_taken_to_prepare_three_burgers)  # Output: 45

# EXAMPLE 2: Variables can be reassigned
# The value stored in a variable can change during program execution
lover = "Sam"
print("I love " + lover)  # Output: I love Sam

lover = "Jack"  # Same variable, new value
print("I love " + lover)  # Output: I love Jack

# Checking the current value of the variable
if lover == "Sam":
    print("Lover is Sam")
elif lover == "Jack":
    print("Lover is Jack")  # This will execute since lover is "Jack"
else:
    print("Lover is not Sam")

# COMMENTED OUT: Examples of printing different data types
# Uncomment these lines to see the values of different types
# print(hello_message)
# print(int_message)
# print(float_message)
# print(bool_message)
# print(list_message)
# print(tuple_message)
# print(dict_message)

# EXAMPLE 3: Variable reassignment demonstration
awesome_variable = "This is an awesome variable"
print(awesome_variable)

# Reassign the variable to a new string
awesome_variable = "This is even more awesome now"
print(awesome_variable)