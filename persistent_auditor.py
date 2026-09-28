inventory = 0
failed_attempts = 0 
deliveries = 0
def get_valid_input() -> int | str:
    entry = input("Enter a stock quantity (or type 'quit' to exit): ")

    if entry.lower() == "quit":
        return "quit"

    if not entry.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        return None

    return quantity


def process_delivery(current_total: int, new_value: int) -> int:
    return current_total + new_value


def calculate_tax(amount: int) -> float:
    tax_rate = 0.10
    return amount * tax_rate


def generate_report(total_units: int, failed_attempts: int, deliveries: int) -> None:
    print("\n--- Inventory Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Failed Attempts: {failed_attempts}")
    print(f"Total Deliveries: {deliveries}")

def main():
    inventory = 0
    failed_attempts = 0
    deliveries = 0

    while True:
        entry = get_valid_input()

        if entry == "quit":
            break

        if entry is None:
            failed_attempts += 1
            continue

        inventory = process_delivery(inventory, entry)
        deliveries += 1
        tax = calculate_tax(entry)
        print(f"Tax for this delivery: ${tax:.2f}")

        if inventory > 500:
            print("Alert: Inventory exceeds 500 units! Stopping audit")
            generate_report(inventory, failed_attempts, deliveries)
            break


    generate_report(inventory, failed_attempts, deliveries)


if __name__ == "__main__":
    main()


