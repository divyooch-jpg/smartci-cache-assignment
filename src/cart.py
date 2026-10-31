from src.pricing import apply_discount


def cart_total(items, discount_percent=0):
    """items: list of (price, quantity) tuples."""
    subtotal = sum(price * qty for price, qty in items)
    return apply_discount(subtotal, discount_percent)
