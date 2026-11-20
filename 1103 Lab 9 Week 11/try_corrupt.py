import os
import tempfile

from main import load_inventory

# Create a temporary file with broken JSON
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as temp:
    temp.write("{ this is not valid json")
    temp_path = temp.name

inventory, suppliers = load_inventory(temp_path)
print("Products loaded:", len(inventory.get_products()))

os.remove(temp_path)