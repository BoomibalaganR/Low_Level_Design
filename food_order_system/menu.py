import uuid

from food_order_system.category import Category


class Menu:
    def __init__(self, name=None):
        self._id = uuid.uuid4()
        self.name = name
        self.categories = []

    @property
    def id(self):
        return str(self._id)

    def add_category(self, category: Category):
        print("adding category...")
        self.categories.append(category)

    def get_category(self):
        print("Getting categories...")

    def remove_category(self, cat_id: int):
        print(f"Removing category with ID: {cat_id}")

    def __str__(self):
        menu_info = f"Menu ID: {self._id}\nCategories:\n"
        if self.categories:
            menu_info += "\n".join([str(category) for category in self.categories])
        else:
            menu_info += "No categories available."
        return menu_info
