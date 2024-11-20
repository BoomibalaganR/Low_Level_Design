import uuid

from food_order_system.cart import Cart


class User:
    def __init__(self, name: str, password: str, email: str):
        self._id = uuid.uuid4()
        self.name = name
        self.password = password
        self.email = email
        self.orders = []
        self.cart = Cart(self)

    @property
    def id(self):
        return str(self._id)

    def login(self, email: str, password: str):
        if self.email != email or self.password != password:
            raise ValueError("Invalid email and password...")

    def update_details(self):
        print("Updating user details...")

    def search_restaurant(self, restaurant_name: str):
        print(f"Searching for restaurant: {restaurant_name}")

    def search_food(self, food_name: str, restaurant_name: str, category: str):
        print(
            f"Searching for food: {food_name} in {restaurant_name}, category: {category}"
        )

    def view_menu(self, restaurant):
        print(f"Viewing menu for restaurant: {restaurant.get_name()}")

    def add_item_to_cart(self, item):
        print(f"Adding item to cart: {item.get_name()}")

    def remove_item_from_cart(self, item):
        print(f"Removing item from cart: {item.get_name()}")

    def check_out(self, orderable, payment_gateway, delivery_details):
        print("Checking out...")
