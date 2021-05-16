def discount_price(discount):
    def discounting(price):
        return price*(1-discount)

    return discounting