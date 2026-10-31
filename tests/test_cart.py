from src.cart import cart_total


def test_cart_total_no_discount():
    assert cart_total([(10, 2), (5, 1)]) == 25.0


def test_cart_total_with_discount():
    assert cart_total([(100, 1)], 10) == 90.0
