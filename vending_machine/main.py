import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vending_machine.machine import VendingMachine
from vending_machine.product import Product


class VendingMachineDemo:
    @staticmethod
    def run():
        machine = VendingMachine()
        machine.add_product(Product("cake", 10, 5))
        machine.add_product(Product("chocolate", 25, 3))

        machine.insert_money(10)
        machine.select_product("cake")
        machine.dispense_product()


if __name__ == "__main__":
    VendingMachineDemo.run()
