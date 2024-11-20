from food_order_system.category import Category
from food_order_system.item import Item
from food_order_system.menu import Menu
from food_order_system.restaurant import Restaurant
from food_order_system.user import User


class OrderService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.users = {}
        self.restaurants = {}
        self.orders = {}

    def restaurant_exits(self, restaurant_name):
        restaurant = self.restaurants.get(restaurant_name)
        if not restaurant:
            raise ValueError("Restaurant not found")
        return restaurant

    # User-related methods
    def user_signup(self, data):
        email = data.get("email")
        if self.users.get(email):
            raise ValueError("Email already exit...")
        self.users[email] = User(**data)
        print(self.users)
        print("User created successfully....!!")

    def user_login(self, email, password):
        user = self.users.get(email)
        if not user:
            raise ValueError("User not found....")

        user.login(email, password)
        print("Successfully login.....")

    def update_user_details(self, user, details):
        """
        Update user details.
        """
        pass

    def search_restaurant(self, restaurant_name):
        """
        Search for a restaurant by name.
        """
        restaurant = self.restaurants.get(restaurant_name)
        if restaurant:
            return restaurant
        return "Restaurant no matched with given name"

    def search_food(self, food_name, restaurant_name, category):
        """
        Search for food items in a restaurant by name or category.
        """
        restaurant = self.restaurants.get(restaurant_name)
        if not restaurant:
            raise ValueError("Restaurant not found")
        restaurant.get_menu()

    def view_menu(self, restaurant):
        """
        Return the menu of a given restaurant.
        """

        return restaurant.get_menu_list() if restaurant else []

    def add_item_to_cart(self, user, item):
        """
        Add an item to the user's cart.
        """
        pass

    def remove_item_from_cart(self, user, item):
        """
        Remove an item from the user's cart.
        """
        pass

    def check_out(self, user, orderable, payment_gateway, delivery_details):
        """
        Handle the checkout process.
        """
        pass

    # Restaurant-related methods
    def add_restaurant(self, data):
        """
        Add a restaurant to the system.
        """
        restaurant_name = data.get("name")
        if self.restaurants.get(restaurant_name):
            raise ValueError("Given restaurant name already exit...")
        self.restaurants[restaurant_name] = Restaurant(**data)
        print(self.restaurants)
        print("successfully added restaurant...")
        return self.restaurants[restaurant_name]

    def create_menu(self, restaurant, data):
        for each_menu in data:
            menu = Menu()
            category = Category(name=each_menu["category"])
            for each_item in each_menu["items"]:
                category.add_item(Item(**each_item))
            menu.add_category(category)
            restaurant.add_menu(menu)

    def get_order_list(self, restaurant):
        """
        Get all orders for a restaurant.
        """
        pass

    def confirm_order(self, order):
        """
        Confirm an order.
        """
        pass

    # Order-related methods
    def cancel_order(self, user, order_id):
        """
        Cancel an order.
        """
        pass

    def list_user_orders(self, user):
        """
        List all orders placed by a user.
        """
        pass

    def list_restaurant_orders(self, restaurant):
        """
        List all orders associated with a restaurant.
        """
        pass
