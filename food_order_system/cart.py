import uuid

from food_order_system.orderable import Orderable

# from food_order_system.user import User


class Cart(Orderable):
    def __init__(self, user: "User"):
        self._id = uuid.uuid4()
        self.user = user
        self.items = []
        self.total_cost = 0.0

    @property
    def id(self):
        return str(self._id)

    def add_item(self, item):
        print("Adding item to cart...")

    def remove_item(self, item_id: int):
        print(f"Removing item with ID: {item_id}")

    def get_item(self, item_id: int):
        print(f"Getting item with ID: {item_id}")

    def place_order(self):
        print("Placing order for cart...")

    def get_cost(self):
        return self.total_cost

    def clear_items(self):
        print("Clearing items in cart...")
