# READING FILES LINE BY LINE
# This file demonstrates how to read a file one line at a time
# This is more memory-efficient for large files

# Open the file in read mode
with open("costs.txt", "r") as file:
    # Iterate through the file object directly - this reads one line at a time
    # This is better than file.read() for large files because it doesn't load
    # the entire file into memory at once
    for line in file:
        # strip() removes whitespace (spaces, tabs, newlines) from both ends
        # This is useful because each line from a file includes a newline character '\n'
        print(line.strip())