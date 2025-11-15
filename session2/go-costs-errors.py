# ERROR HANDLING IN PYTHON
# This file demonstrates how to handle errors gracefully when processing data
# Use try-except blocks to prevent crashes when encountering invalid data

# Initialize tracking variables
total_cost = 0
over_budget = []
errors = []  # List to track all errors encountered

# Process a CSV file that may contain errors
with open("costs-with-errors.csv", "r") as file:
    next(file)  # Skip header

    # enumerate() gives us both the line number and the line content
    # start=2 because line 1 is the header (which we skip)
    for line_num, line in enumerate(file, start=2):
        # TRY-EXCEPT block: Try to execute code, catch errors if they occur
        try:
            # Attempt to parse and process the line
            service, cost = line.strip().split(",")
            daily_cost = float(cost)  # This might fail if cost is not a number
            monthly_cost = daily_cost * 30
            total_cost += monthly_cost

            if daily_cost > 3.00:
                over_budget.append(service)

            print(f"{service}: ${monthly_cost:.2f}/month")

        # Catch specific error: ValueError occurs when conversion fails
        # Example: float("abc") raises ValueError
        except ValueError as e:
            error_msg = f"Error on line {line_num}: Invalid cost value '{cost}' for service '{service}'"
            errors.append(error_msg)
            print(f"⚠️  {error_msg}")

        # Catch all other errors (like split() failing, etc.)
        # This is a safety net for unexpected issues
        except Exception as e:
            error_msg = f"Error on line {line_num}: {str(e)}"
            errors.append(error_msg)
            print(f"⚠️  {error_msg}")

# Print summary (program continues even if errors occurred)
print(f"\nTotal: ${total_cost:.2f}")
print(f"Over budget: {', '.join(over_budget)}")

# Report all errors at the end if any were encountered
if errors:
    print(f"\n⚠️  {len(errors)} error(s) encountered:")
    for error in errors:
        print(f"   - {error}")