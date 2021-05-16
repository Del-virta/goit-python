DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    discount = customer.get('discount', DEFAULT_DISCOUNT)
    price = price*(1-discount)
    return price 