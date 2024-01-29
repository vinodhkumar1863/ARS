'''  Problem Statement: Develop a Python program for an airline reservation system with the following features:

1.Create a Flight class to represent each flight with attributes such as flight number, destination, departure time, and available seats.
2.Implement methods to book a seat on a flight, cancel a booked seat, display available seats for a flight, and display all booked seats for a flight.
3.Use data structures and algorithms to efficiently manage seat bookings and availability for each flight.
4.Implement error handling for cases such as booking a seat that is already booked, canceling a seat that is not booked, or displaying available/booked seats for a non-existent flight.



'''


class Flight:
    def __init__(self, flight_number, destination, departure_time, total_seats):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.available_seats = total_seats
        self.booked_seats = []

    def book_seat(self, seat_number):
        if self.available_seats > 0:
            if seat_number not in self.booked_seats:
                self.booked_seats.append(seat_number)
                self.available_seats -= 1
                print(f"Seat {seat_number} booked successfully for flight {self.flight_number}.")
            else:
                print(f"Seat {seat_number} is already booked.")
        else:
            print("No available seats for this flight.")

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            self.available_seats += 1
            print(f"Seat {seat_number} canceled successfully for flight {self.flight_number}.")
        else:
            print(f"Seat {seat_number} is not booked for this flight.")

    def display_available_seats(self):
        print(f"Available seats for flight {self.flight_number}: {self.available_seats}")

    def display_booked_seats(self):
        print(f"Booked seats for flight {self.flight_number}: {self.booked_seats}")


# Test the airline reservation system
flight1 = Flight("FL001", "New York", "10:00", 100)

flight1.book_seat("A1")
flight1.book_seat("A2")
flight1.display_available_seats()
flight1.display_booked_seats()

flight1.cancel_seat("A2")
flight1.display_available_seats()
flight1.display_booked_seats()

flight1.book_seat("A1")  # Try booking the ticket already booked,to check error handling