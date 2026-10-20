def calculate_total(price, quantity):
    return price + quantity  # Existing bug


def apply_discount(total, discount_percent):
    return total * (1 - discount_percent / 100)
