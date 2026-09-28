import os

def load_orders(filename: str = "orders.txt") -> list[tuple[int, str, int]]:
    """Load existing orders from file. Returns list of (id, product, qty)."""
    if not os.path.exists(filename):
        return []
    orders = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                order_id = int(parts[0])
                product = parts[1].strip()
                qty = int(parts[2])
                orders.append((order_id, product, qty))
    return orders


def save_orders(orders: list[tuple[int, str, int]], filename: str = "orders.txt") -> None:
    """Save all orders back to file."""
    with open(filename, "w") as f:
        for order_id, product, qty in orders:
            f.write(f"{order_id}, {product}, {qty}\n")


def display_orders(orders: list[tuple[int, str, int]]) -> None:
    print("\nCurrent Orders:")
    for order_id, product, qty in orders:
        print(f"{order_id}, {product}, {qty}")


def main():
    orders = load_orders()

    # Show existing orders
    display_orders(orders)

    # Get new order
    product = input("\nEnter product name: ")
    qty_str = input("Enter quantity: ")

    if not qty_str.isdigit():
        print("Error: Quantity must be a number.")
        return

    qty = int(qty_str)

    # Assign next order ID
    next_id = orders[-1][0] + 1 if orders else 1001

    new_order = (next_id, product, qty)
    orders.append(new_order)

    print("\nNew order added:")
    print(f"{next_id}, {product}, {qty}")

    save_orders(orders)
    print("\nOrder successfully saved to orders.txt")


if __name__ == "__main__":
    main()
