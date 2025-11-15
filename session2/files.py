# READING FILES IN PYTHON
# This file demonstrates how to read the entire contents of a file at once

# The 'with' statement is the recommended way to work with files
# It automatically closes the file when done, even if an error occurs
# "r" means read mode (the file must exist)
with open("costs.txt", "r") as file:
    # file.read() reads the ENTIRE file content as a single string
    content = file.read()
    print(content)

# Note: The file is automatically closed after the 'with' block ends
# You don't need to call file.close() manually