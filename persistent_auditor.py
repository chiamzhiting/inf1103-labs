import os

def load_inventory(filename: str = "inventory.txt") -> tuple[int, list[int]]:
    """Load inventory total and history from file. Returns (total_units, history_list)."""
    if not os.path.exists(filename):
        return 0, []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            total_units = int(lines[0].strip())
            history = [int(x.strip()) for x in lines[1:]]
            return total_units, history
    except Exception:
        return 0, []

def main():
    inventory, history = load_inventory()
    print("Loaded inventory:", inventory)
    print("History:", history)

if __name__ == "__main__":
    main()

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

def main():
    inventory, history = load_inventory()
    failed_attempts = 0
    deliveries = len(history)

    while True:
        entry = get_valid_input()
        if entry == "quit":
            break
        if entry is None:
            failed_attempts += 1
            continue

        inventory = process_delivery(inventory, entry)
        history.append(entry)
        deliveries += 1
        print(f"Transaction recorded: {entry} units")

    print("Final inventory:", inventory)
    print("Transaction history:", history)

def save_inventory(total_units: int, history: list[int], filename: str = "inventory.txt") -> None:
    """Save inventory total and history to file."""
    with open(filename, "w") as f:
        f.write(f"{total_units}\n")
        for amount in history:
            f.write(f"{amount}\n")

def main():
    inventory, history = load_inventory()
    failed_attempts = 0
    deliveries = len(history)

    while True:
        entry = get_valid_input()
        if entry == "quit":
            break
        if entry is None:
            failed_attempts += 1
            continue

        inventory = process_delivery(inventory, entry)
        history.append(entry)
        deliveries += 1
        print(f"Transaction recorded: {entry} units")

    print("Final inventory:", inventory)
    print("Transaction history:", history)
    save_inventory(inventory, history)
    print("Inventory successfully saved to inventory.txt")
