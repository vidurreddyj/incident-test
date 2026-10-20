def calculate_total(price, quantity):
    return price + quantity  # Existing bug


def apply_discount(total, discount_percent):
    return total * (1 - discount_percent / 100)


def calculate_shipping(order_total):
    if order_total >= 50:
        return 0
    return 5
