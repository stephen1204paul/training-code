# LOOPS IN PYTHON
# This file demonstrates two main types of loops: for loops and while loops

# Example 1: For Loop
# Use a for loop to iterate through each item in a collection (list, tuple, etc.)
regions = ["us", "eu", "asia"]

# The for loop will execute the indented code once for each item in the list
# 'region' is the loop variable that takes on each value from the list
for region in regions:
    # f-strings (f"...") allow you to embed variables directly in strings using {}
    print(f"Deploy to {region}")

# Example 2: While Loop
# Use a while loop when you want to repeat code until a condition becomes False
retries = 0
max_retries = 3

# The while loop checks the condition before each iteration
# It continues as long as the condition is True
while retries < max_retries:
    print(f"Attempt {retries}")
    # IMPORTANT: Always modify the loop variable to eventually make the condition False
    # Otherwise, you'll create an infinite loop!
    retries += 1  # Shorthand for: retries = retries + 1