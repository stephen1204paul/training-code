# CONDITIONAL STATEMENTS (if/else/elif)
# This file demonstrates how to make decisions in Python using conditional statements

# Example 1: Simple if-else statement
# Compare two values and execute different code based on the result
cost = 150
budget = 100

# The 'if' statement checks if a condition is True
# If cost is greater than budget, execute the indented code block
if cost > budget:
    print("Over budget!")
else:
    # The 'else' block runs when the if condition is False
    print("Within budget")

# Example 2: if-elif-else chain
# Use 'elif' (else if) to check multiple conditions in sequence
vm_count = 25

# Python checks each condition from top to bottom
# Once a condition is True, it executes that block and skips the rest
if vm_count < 10:
    print("Small")
elif vm_count < 50:
    # This condition is True (25 < 50), so this block executes
    print("Medium")
else:
    # This runs only if all above conditions are False
    print("Large")

