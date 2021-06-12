class FoodComponent:
    def __init__(self, product_names, weight, price):
        self.product_names = product_names
        self.weight = weight
        self.price = price

    def __str__(self):
        return f'Product {str(self.product_names)}, weight = {self.weight}, price = {self.price}'

    def __add__(self, other):
        self.product_names+=other.product_names
        self.weight+=other.weight
        self.price+=other.price
        return FoodComponent(self.product_names, self.weight, self.price)