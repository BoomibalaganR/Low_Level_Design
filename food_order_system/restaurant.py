import uuid


class Restaurant:
    def __init__(self, name: str, location: str, contact_details: str):
        self._id = uuid.uuid4()
        self.name = name
        self.menus = []
        self.location = location
        self.contact_details = contact_details
        self.orders = []

    @property
    def id(self):
        return str(self._id)

    def get_menu(self, menu_id: int):
        print(f"Getting menu with ID: {menu_id}")

    def get_menu_list(self):
        return self.menus

    def add_menu(self, menu):
        print("Adding menu...")
        self.menus.append(menu)

    def update_menu(self, menu):
        print("Updating menu...")

    def remove_menu(self, menu_id: int):
        print(f"Removing menu with ID: {menu_id}")

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_contact_details(self):
        return self.contact_details

    def confirm_order(self, order):
        print("Confirming order...")

    def get_order_list(self):
        print("Getting order list...")

    def __str__(self) -> str:
        print(f"Id {self.id} - {self.name} - {self.location}")
