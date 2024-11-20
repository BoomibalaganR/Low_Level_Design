import uuid

from food_order_system.orderable import Orderable


class Item(Orderable):
    def __init__(self, name: str, description: str, price: float):
        self._id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price

    @property
    def id(self):
        return str(self._id)

    def get_price(self):
        return self.price

    def set_price(self, price: float):
        print("Setting price...")

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        print("Setting name...")

    def place_order(self):
        print("Placing order for item...")

    def __str__(self):
        return f"\tItem: {self.name} (ID: {self._id})\n\t Description: {self.description}\n\tPrice: ${self.price:.2f}"
