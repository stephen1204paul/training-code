# WRITING TO FILES
# This file demonstrates how to create a new file or overwrite an existing file

# Store the data you want to write
data = "Total Cost: $250"

# "w" means write mode
# WARNING: This will OVERWRITE the file if it already exists!
# If the file doesn't exist, it will be created
with open("report.txt", "w") as file:
    # file.write() writes the string to the file
    # Note: write() doesn't automatically add newlines, you need to include \n if needed
    file.write(data)