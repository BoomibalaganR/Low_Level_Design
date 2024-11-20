from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_coin(self, machine, amount):
        raise NotImplementedError

    @abstractmethod
    def select_product(self, machine, product):
        raise NotImplementedError

    @abstractmethod
    def dispense_product(self, machine):
        raise NotImplementedError


class IdleState(State):
    def insert_coin(self, machine, amount):
        machine.set_amount(amount)
        print(f"insert money {amount}")
        machine.set_state(machine.select_product_state)

    def select_product(self, machine, product):
        raise NotImplementedError

    def dispense_product(self, machine):
        raise NotImplementedError


class SelectProductState(State):
    def select_product(self, machine, product_name):
        selected_product = machine.get_product(product_name)
        if selected_product and selected_product.is_available():
            print(f"selected product {selected_product.get_name()}")
            machine.set_selected_product(selected_product)
            machine.set_state(machine.dispense_product_state)

    def insert_coin(self, machine, amount):
        raise NotImplementedError

    def dispense_product(self, machine):
        raise NotImplementedError


class dispenseProductState(State):
    def dispense_product(self, machine):
        dispense_product = machine.get_selected_product()
        if dispense_product:
            dispense_product.reduce_quantity(1)
            machine.add_total_selling_amount(dispense_product.get_price())
            machine.set_selected_product(None)
            print(
                f"successfully dispense product {dispense_product.get_name()} {dispense_product.get_price()}"
            )
        return dispense_product

    def insert_coin(self, machine, amount):
        raise NotImplementedError

    def select_product(self, machine, product):
        pass
