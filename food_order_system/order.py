import uuid

from food_order_system.orderstate import PendingState
from food_order_system.restaurant import Restaurant
from food_order_system.user import User


class Order:
    def __init__(
        self,
        user: User,
        items: list,
        total_cost: float,
        restaurant: Restaurant,
    ):
        self._id = uuid.uuid4()
        self.user = user
        self.items = items
        self.state = PendingState()
        self.total_cost = total_cost
        self.restaurant = restaurant
        self.payment_type = None
        self.delivery = None

    @property
    def id(self):
        return str(self._id)

    def change_state(self, state: "OrderState"):
        print("Changing order state...")

    def get_order_details(self):
        print("Getting order details...")

    def confirm(self):
        print("Order confirmed.")

    def progress(self):
        print("Order in progress.")

    def deliver(self):
        print("Order delivered.")

    def cancel(self):
        print("Order canceled.")
