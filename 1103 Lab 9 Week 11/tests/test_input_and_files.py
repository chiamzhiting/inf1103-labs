from inventory import Inventory
from main import get_positive_float, load_products, load_inventory

CSV_TEXT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


def test_get_positive_float_keeps_asking(monkeypatch, capsys):
    answers = iter(["abc", "-5", "12.50"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    result = get_positive_float("Price: ")

    out = capsys.readouterr().out
    assert result == 12.5
    assert "valid number" in out
    assert "greater than zero" in out


def test_load_products_skips_bad_rows_and_loads_good_ones(tmp_path, supplier, capsys):
    csv_file = tmp_path / "products.csv"
    csv_file.write_text(CSV_TEXT)
    inventory = Inventory()

    load_products(str(csv_file), inventory, supplier)

    out = capsys.readouterr().out
    ids = [p.get_product_id() for p in inventory.get_products()]
    assert ids == ["P001", "D001", "P003"]
    assert out.index("S001") < out.index("P002") < out.index("3 products loaded.")
    assert out.rstrip().endswith("Load attempt finished.")


def test_load_products_missing_file_is_handled(tmp_path, supplier, capsys):
    inventory = Inventory()

    load_products(str(tmp_path / "nope.csv"), inventory, supplier)

    out = capsys.readouterr().out
    assert "not found" in out
    assert "Load attempt finished." in out
    assert "products loaded" not in out
    assert inventory.get_products() == []


def test_corrupt_inventory_file_is_handled(tmp_path, capsys):
    bad_file = tmp_path / "inventory.json"
    bad_file.write_text("{ this is not valid json")

    inventory, suppliers = load_inventory(str(bad_file))

    assert inventory.get_products() == []
    assert "empty or damaged" in capsys.readouterr().out