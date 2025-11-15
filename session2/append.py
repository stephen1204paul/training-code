# APPENDING TO FILES
# This file demonstrates how to add content to the end of an existing file

# The \n at the start creates a new line before our text
# This ensures the new content appears on a separate line
new_data = "\nVM Cost: $50"

# "a" means append mode
# This adds content to the END of the file without deleting existing content
# If the file doesn't exist, it will be created (just like "w" mode)
with open("report.txt", "a") as file:
    # Write the new data to the end of the file
    file.write(new_data)