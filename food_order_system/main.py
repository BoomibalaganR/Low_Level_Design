import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from food_order_system.order_service import OrderService


class FoodOrderServiceDemo:
    @staticmethod
    def run():
        order_service = OrderService()
        data = {
            "name": "Boomi",
            "email": "boomibalagan@gmail.com",
            "password": "dev123",
        }
        order_service.user_signup(data)
        # user_login
        order_service.user_login(email="boomibalagan@gmail.com", password="dev123")

        restaurant_data = {
            "name": "ovm restaturant",
            "location": "kumbakanam",
            "contact_details": "main road, kumbakonam",
        }
        ovm_restaurant = order_service.add_restaurant(restaurant_data)
        menu_data = [
            {
                "category": "Drinks",
                "items": [
                    {
                        "name": "Coca-Cola",
                        "price": 1.99,
                        "description": "Refreshing cold drink",
                    },
                    {
                        "name": "Lemonade",
                        "price": 2.49,
                        "description": "Freshly squeezed lemonade",
                    },
                    {
                        "name": "Iced Coffee",
                        "price": 3.49,
                        "description": "Chilled coffee with ice",
                    },
                ],
            },
            {
                "category": "Snacks",
                "items": [
                    {
                        "name": "French Fries",
                        "price": 2.99,
                        "description": "Crispy golden fries",
                    },
                    {
                        "name": "Nachos",
                        "price": 4.99,
                        "description": "Tortilla chips with cheese dip",
                    },
                    {
                        "name": "Onion Rings",
                        "price": 3.49,
                        "description": "Crispy onion rings served with dip",
                    },
                ],
            },
            {
                "category": "Veg",
                "items": [
                    {
                        "name": "Vegetable Burger",
                        "price": 5.99,
                        "description": "Veggie patty in a whole wheat bun",
                    },
                    {
                        "name": "Grilled Veg Sandwich",
                        "price": 4.99,
                        "description": "Grilled sandwich with fresh vegetables",
                    },
                    {
                        "name": "Veggie Pizza",
                        "price": 8.99,
                        "description": "Pizza topped with fresh vegetables and cheese",
                    },
                ],
            },
            {
                "category": "Non-Veg",
                "items": [
                    {
                        "name": "Chicken Wings",
                        "price": 6.99,
                        "description": "Spicy grilled chicken wings",
                    },
                    {
                        "name": "Beef Burger",
                        "price": 7.99,
                        "description": "Juicy beef patty in a sesame bun",
                    },
                    {
                        "name": "Pepperoni Pizza",
                        "price": 9.99,
                        "description": "Pizza topped with pepperoni and cheese",
                    },
                ],
            },
        ]
        order_service.create_menu(ovm_restaurant, menu_data)
        restaurant_menus = order_service.view_menu(ovm_restaurant)
        for each_menu in restaurant_menus:
            print(each_menu)


if __name__ == "__main__":
    FoodOrderServiceDemo.run()
