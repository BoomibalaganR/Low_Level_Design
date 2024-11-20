class Car:
    _id_counter = 0

    def __init__(self, type, rental_price, location) -> None:
        Car._id_counter += 1
        self._id = Car._id_counter
        self._type = type
        self._rental_price = rental_price
        self._location = location
        self._booking = []

    @property
    def id(self):
        return self._id

    def add_booking(self, booking):
        self._booking.append(booking)

    def is_available(self, start_date, end_date):
        for booking in self._booking:
            if not (end_date <= booking._start_date or start_date >= booking._end_date):
                return False
        return True

    def __str__(self):
        return f"Car ID: {self._id}, Type: {self._type}, Price: {self._rental_price}, Location: {self._location}"
