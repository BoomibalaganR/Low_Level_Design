from vending_machine.state import IdleState, SelectProductState, dispenseProductState


class VendingMachine:
    def __init__(self) -> None:
        self._product = {}
        self._total_selling_amount = 0
        self._amount = 0
        self.select_product_state = SelectProductState()
        self.dispense_product_state = dispenseProductState()
        self._state = IdleState()
        self._selected_product = None

    def add_product(self, product):
        self._product[product.get_name()] = product

    def get_product(self, product_name):
        return self._product[product_name]

    def set_state(self, state):
        self._state = state

    def set_amount(self, amount):
        self._amount += amount

    def get_amount(self):
        return self._amount

    def add_total_selling_amount(self, amount):
        self._total_selling_amount += amount

    def get_total_selling_amount(self):
        return self._total_selling_amount

    def set_selected_product(self, product):
        self._selected_product = product

    def get_selected_product(self):
        return self._selected_product

    def insert_money(self, amount):
        self._state.insert_coin(self, amount)

    def select_product(self, product_name):
        self._state.select_product(self, product_name)

    def dispense_product(self):
        self._state.dispense_product(self)
