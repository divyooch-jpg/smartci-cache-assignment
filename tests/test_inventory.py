import pytest
from src.inventory import Inventory


def test_add_and_remove():
    inv = Inventory()
    inv.add("pen", 5)
    inv.remove("pen", 2)
    assert inv.stock["pen"] == 3


def test_remove_too_many():
    inv = Inventory()
    with pytest.raises(ValueError):
        inv.remove("pen", 1)
