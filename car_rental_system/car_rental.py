from car_rental_system.booking import Booking
from car_rental_system.payment import GpayPayment, PaymentContext


class CarRental:
    def __init__(self) -> None:
        self._booking = {}
        self._cars = {}
        self._payment_gateway = PaymentContext(GpayPayment())

    def add_car(self, car):
        self._cars[car.id] = car

    def search_car(self, start_date, end_date, car_type=None):
        available_cars = []

        for car in self._cars.values():
            if car.is_available(start_date, end_date):
                if car_type is None or car._type == car_type:
                    available_cars.append(car)
        return available_cars

    def book_car(self, car_id, customer_name, start_date, end_date):
        car = self._cars.get(car_id)
        if not car:
            print(f"Car with ID {car_id} not found.")
            return None
        if not car.is_available(start_date, end_date):
            print(f"Car with ID {car_id} is not available for the given dates.")
            return None
        new_booking = Booking(car, customer_name, start_date, end_date)
        new_booking.calculate_total_cost()

        car.add_booking(new_booking)
        self._booking[new_booking.id] = new_booking
        return new_booking

    def make_payment(self, booking_id, amount):
        if not self._payment_gateway.process_payment(amount):
            raise ValueError("Payment failed")
        print("payment success....")
        return True

    def confirm_booking(self, booking_id, payment_strategy=None):
        if payment_strategy:
            self._payment_gateway.set_strategy(payment_strategy)

        booking = self._booking.get(booking_id)
        if not booking:
            raise ValueError(f"Booking ID {booking_id} not found")

        if self.make_payment(booking.id, booking.get_total_cost()):
            booking.set_booking_status("confirmed")
            booking.set_payment_status("paid")
        print("Booking confirmed....")
