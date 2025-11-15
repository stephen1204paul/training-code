# WORKING WITH LISTS IN PYTHON
# This file demonstrates creating lists and performing common list operations

# CREATING LISTS
# Lists are ordered collections that can hold any type of data
vm_names = ["web-1", "web-2", "db-1"]
lunch_ideas = ["burger", "pizza", "salad", "mamak", "wantan mee"]
costs = [0.05, 0.05, 0.10]
empty_list = []  # Empty list that can be filled later

# ACCESSING LIST ELEMENTS
# Lists use zero-based indexing: first item is at index 0
# Uncomment to try:
# first_vm = vm_names[0]  # Gets "web-1"
# print(first_vm)

# ADDING ITEMS TO A LIST
# append() adds an item to the end of the list
# Uncomment to try:
# vm_names.append("db-2")  # Adds "db-2" to the end
# print(vm_names)  # Output: ["web-1", "web-2", "db-1", "db-2"]

# REMOVING ITEMS FROM A LIST
# remove() deletes the first occurrence of a specific value
# Uncomment to try:
# vm_names.remove("web-2")  # Removes "web-2" from the list
# print(vm_names)  # Output: ["web-1", "db-1"]

# GETTING LIST LENGTH
# len() returns the number of items in the list
# Uncomment to try:
# list_length = len(vm_names)
# print(list_length)  # Output: 3

# MODIFYING LIST ELEMENTS
# You can change an item by assigning a new value to a specific index
# Uncomment to try:
# lunch_ideas[1] = "sushi"  # Changes "pizza" (at index 1) to "sushi"
# print(lunch_ideas[1])  # Output: sushi

# ITERATING THROUGH A LIST
# Use a for loop to process each item in the list
for lunch in lunch_ideas:
    # This will run once for each item in the list
    print("I want to eat " + lunch)