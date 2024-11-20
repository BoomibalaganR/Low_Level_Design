class PaymentGateway:
    def pay(self, amount: float):
        print("Processing payment...")

    def get_payment_type(self):
        print("Getting payment type...")


class GPay(PaymentGateway):
    def pay(self, amount: float):
        print("Processing GPay payment...")

    def get_payment_type(self):
        return "GPay"


class CashOnDelivery(PaymentGateway):
    def pay(self, amount: float):
        print("Cash on Delivery selected.")

    def get_payment_type(self):
        return "Cash on Delivery"
