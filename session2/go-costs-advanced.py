# PROCESSING CSV FILES - ADVANCED EXAMPLE
# This file is similar to go-costs-basic.py but uses a different CSV file
# The code structure is the same, demonstrating reusability of the pattern

# Initialize tracking variables
total_cost = 0
over_budget = []

# Read from a different CSV file (costs-advanced.csv)
# This might contain more services or different cost values
with open("costs-advanced.csv", "r") as file:
    # Skip the header row
    next(file)

    # Process each service entry
    for line in file:
        # Parse the CSV line
        service, cost = line.strip().split(",")

        # Convert and calculate costs
        daily_cost = float(cost)
        monthly_cost = daily_cost * 30
        total_cost += monthly_cost

        # Track services exceeding budget threshold
        if daily_cost > 3.00:
            over_budget.append(service)

        # Display individual service costs
        print(f"{service}: ${monthly_cost:.2f}/month")

# Print summary
print(f"\nTotal: ${total_cost:.2f}")
print(f"Over budget: {', '.join(over_budget)}")