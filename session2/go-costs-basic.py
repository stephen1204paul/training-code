# PROCESSING CSV FILES - BASIC EXAMPLE
# This file demonstrates reading and processing a CSV (Comma-Separated Values) file
# to calculate cloud service costs

# Initialize variables to track totals and issues
total_cost = 0
over_budget = []  # List to store services that exceed the budget threshold

# Open and read the CSV file
with open("costs-basic.csv", "r") as file:
    # Skip the header row (first line with column names)
    next(file)

    # Process each line in the file
    for line in file:
        # Split the line by comma to extract service name and cost
        # Example line: "EC2,2.50" becomes ["EC2", "2.50"]
        service, cost = line.strip().split(",")

        # Convert the cost string to a floating-point number
        daily_cost = float(cost)

        # Calculate monthly cost (30 days)
        monthly_cost = daily_cost * 30

        # Add to running total
        total_cost += monthly_cost

        # Check if this service is over the daily budget threshold
        if daily_cost > 3.00:
            over_budget.append(service)

        # Display the monthly cost for this service
        # :.2f formats the number to 2 decimal places
        print(f"{service}: ${monthly_cost:.2f}/month")

# Print summary information
print(f"\nTotal: ${total_cost:.2f}")
# join() combines list items into a single string separated by ', '
print(f"Over budget: {', '.join(over_budget)}")