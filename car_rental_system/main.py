import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from datetime import datetime

# from car_rental_system.car import Car
# from car_rental_system.car_rental import CarRental


# class CarRentelDemo:
#     @staticmethod
#     def run():
#         api = CarRental()
#         c1 = Car("SUV", 100, "LOCATION-A")
#         c2 = Car("luxury", 500, "LOCATION-B")

#         api.add_car(c1)
#         api.add_car(c2)

#         start_date = datetime.strptime("2024-09-30", "%Y-%m-%d")
#         end_date = datetime.strptime("2024-10-05", "%Y-%m-%d")

#         car_list = api.search_car(start_date, end_date)
#         if car_list:
#             print("Available cars:")
#             for car in car_list:
#                 print(car)
#         else:
#             print("No cars available for the given dates.")

#         selected_car = car_list[0]
#         booking = api.book_car(selected_car.id, "BOOMI", start_date, end_date)
#         if booking:
#             print(booking)
#             api.confirm_booking(booking.id)

#         # try book same car at same time frame
#         bk = api.book_car(selected_car.id, "ROLEX", start_date, end_date)
#         print(bk)


# if __name__ == "__main__":
#     CarRentelDemo.run()
from datetime import datetime

from car_rental_system.car import Car
from car_rental_system.car_rental import CarRental


class CarRentalClient:
    def __init__(self):
        self.api = CarRental()
        self._setup_cars()

    def _setup_cars(self):
        self.api.add_car(Car("SUV", 100, "LOCATION-A"))
        self.api.add_car(Car("Luxury", 500, "LOCATION-B"))

    def display_menu(self):
        print("\n--- Car Rental System ---")
        print("1. Search Car")
        print("2. Book Car")
        print("3. Confirm Booking")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.search_car()
            elif choice == "2":
                self.book_car()
            elif choice == "3":
                self.confirm_booking()
            elif choice == "4":
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please try again.")

    def search_car(self):
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        car_list = self.api.search_car(start_date, end_date)

        if car_list:
            print("Available cars:")
            for car in car_list:
                print(
                    f"{car.id}: {car._type} at {car._location} for ${car._rental_price}/day"
                )
        else:
            print("No cars available for the given dates.")

    def book_car(self):
        car_id = int(input("Enter car ID to book: "))
        customer_name = input("Enter your name: ")
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        booking = self.api.book_car(car_id, customer_name, start_date, end_date)
        if booking:
            print(f"Please confirm the Booking with Booking ID: {booking.id}")
        else:
            print("Booking failed. Please check availability.")

    def confirm_booking(self):
        booking_id = int(input("Enter booking ID to confirm: "))
        try:
            self.api.confirm_booking(booking_id)
            print("Booking confirmed successfully.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    client = CarRentalClient()
    client.run()
