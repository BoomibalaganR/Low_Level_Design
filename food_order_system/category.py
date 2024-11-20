import uuid


class Category:
    def __init__(self, name):
        self._id = uuid.uuid4()
        self.name = name
        self.items = []

    @property
    def id(self):
        return str(self._id)

    def add_item(self, item):
        print("Adding item to category...")
        self.items.append(item)

    def get_item(self, item_id: int):
        print(f"Getting item with ID: {item_id}")

    def update_item(self, item, item_id: int):
        print(f"Updating item with ID: {item_id}")

    def remove_item(self, item_id: int):
        print(f"Removing item with ID: {item_id}")

    def __str__(self):
        category_info = f"  Category: {self.name} (ID: {self._id})\n  Items:\n"
        if self.items:
            category_info += "\n".join([str(item) for item in self.items])
        else:
            category_info += "  No items available."
        return category_info
