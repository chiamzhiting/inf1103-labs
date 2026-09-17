inventory = 0
while True:
    entry = input("Enter a stock quantity (or type 'quit' to exit): ")

    if entry.lower() == "quit":
        print(f"Total Units Processed: {inventory}")
        break

    if not entry.isdigit():
        print("Error: Please enter a valid integer.")
        continue

    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        continue

    inventory += quantity
    if inventory > 500:
        print("Alert: Inventory exceeds 500 units! Stopping audit")
        print(f"Final Total Units Processed: {inventory}")
        break