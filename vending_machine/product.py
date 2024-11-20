class Product:
    def __init__(self, name, price, quantity) -> None:
        self._name = name
        self._price = price
        self._quantity = quantity

    def is_available(self):
        return self._quantity > 0

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def reduce_quantity(self, quantity):
        self._quantity -= quantity

    def get_quantity(self):
        return self._quantity
