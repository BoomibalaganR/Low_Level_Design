class Booking:
    _id_counter = 0

    def __init__(self, car, customer_name, start_date, end_date) -> None:
        Booking._id_counter += 1
        self._id = Booking._id_counter
        self._customer_name = customer_name
        self._car = car
        self._status = "pending"
        self._start_date = start_date
        self._end_date = end_date
        self._payment_status = "pending"
        self._total_cost = 0

    @property
    def id(self):
        return self._id

    def calculate_total_cost(self):
        duration = (self._end_date - self._start_date).days
        self._total_cost = duration * self._car._rental_price

    def get_total_cost(self):
        return self._total_cost

    def set_booking_status(self, status):
        self._status = status

    def set_payment_status(self, status):
        self._payment_status = status

    def __str__(self):
        return f"\nBooking ID: {self._id}, Customer Name: {self._customer_name}, Status: {self._status}, Cost: {self._total_cost}, Payment status: {self._status}, "
