from food_order_system.order import Order


class OrderState:
    def confirm(self, order: Order):
        print("Confirming order state...")

    def progress(self, order: Order):
        print("Order is now in progress...")

    def deliver(self, order: Order):
        print("Delivering order...")

    def cancel(self, order: Order):
        print("Cancelling order...")


class PendingState(OrderState):
    def confirm(self, order: Order):
        print("Order confirmed from pending state.")
        order.change_state(ConfirmedState())  # Transition to ConfirmedState


class ConfirmedState(OrderState):
    def progress(self, order: Order):
        print("Order is now in progress.")
        order.change_state(InProgressState())  # Transition to InProgressState


class InProgressState(OrderState):
    def deliver(self, order: Order):
        print("Order delivered.")
        order.change_state(DeliveredState())  # Transition to DeliveredState


class DeliveredState(OrderState):
    def cancel(self, order: Order):
        print("Cannot cancel, order already delivered.")


class CanceledState(OrderState):
    def cancel(self, order: Order):
        print("Order is already canceled.")
