from abc import ABC

"""
1. What is an online movie ticket booking system?
A movie ticket booking system provides its customers the ability to purchase theatre seats online.
E-ticketing systems allow the customers to browse through movies currently being played and to book seats,
anywhere anytime

2. Requirements and Goals of the System
Our ticket booking service should meet the following requirements:

Functional Requirements:
a. Our ticket booking service should be able to list different cities where its affiliate cinemas are
located.
b. Once the user selects the city, the service should display the movies released in that particular city.
c. Once the user selects a movie, the service should display the cinemas running that movie and its
available showtimes.
d. The user should be able to choose a show at a particular cinema and book their tickets.
e. The service should be able to show the user the seating arrangement of the cinema hall. The user
should be able to select multiple seats according to their preference.
f. The user should be able to distinguish available seats from booked ones.
g. Users should be able to put a hold on the seats for five minutes before they make a payment to
finalize the booking.
h. The user should be able to wait if there is a chance that the seats might become available, e.g., when
holds by other users expire.
i. Waiting customers should be serviced in a fair, first come, first serve manner.

Non-Functional Requirements:
a. The system would need to be highly concurrent. There will be multiple booking requests for the same
seat at any particular point in time. The service should handle this gracefully and fairly.
b. The core thing of the service is ticket booking, which means financial transactions. This means that
the system should be secure and the database ACID compliant.

3. Some Design Considerations:
a. For simplicity, let’s assume our service does not require any user authentication.
b. The system will not handle partial ticket orders. Either user gets all the tickets they want or they
get nothing.
c. Fairness is mandatory for the system.
d. To stop system abuse, we can restrict users from booking more than ten seats at a time.
e. We can assume that traffic would spike on popular/much-awaited movie releases and the seats would
fill up pretty fast. The system should be scalable and highly available to keep up with the surge in
traffic.

4. Capacity Estimation
Traffic estimates: Let’s assume that our service has 3 billion page views per month and sells 10
million tickets a month.

Storage estimates: Let’s assume that we have 500 cities and, on average each city has ten cinemas. If
there are 2000 seats in each cinema and on average, there are two shows every day.

Let’s assume each seat booking needs 50 bytes (IDs, NumberOfSeats, ShowID, MovieID, SeatNumbers,
SeatStatus, Timestamp, etc.) to store in the database. We would also need to store information about
movies and cinemas; let’s assume it’ll take 50 bytes. So, to store all the data about all shows of all
cinemas of all cities for a day:

        500 cities * 10 cinemas * 2000 seats * 2 shows * (50+50) bytes = 2GB / day

To store five years of this data, we would need around 3.6TB.

5. System APIs: search_movies and reserve_seats



user --> web server--> application server

user --search movie

Question: How to handle the cases where two persons are trying to access the 
same seat almost same time?

Ans: We can use transactions in SQL databases to avoid any clashes. For example, if we are using 
SQL server we can utilize Transaction Isolation Levels 2 to lock the rows before we can update 
them. Here is the sample code:

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

BEGIN TRANSACTION;

    -- Suppose we intend to reserve three seats (IDs: 54, 55, 56) for ShowID=99 
    Select * From Show_Seat where ShowID=99 && ShowSeatID in (54, 55, 56) && Status=0 -- free 

    -- if the number of rows returned by the above statement is three, we can update to 
    -- return success otherwise return failure to the user.
    update Show_Seat ...
    update Booking ...

COMMIT TRANSACTION;
‘Serializable’ is the highest isolation level and guarantees safety from Dirty 
2, Nonrepeatable 1 and Phantoms 1 reads. 

One thing to note here, within a transaction if we read rows we get a write lock on them so that 
they can’t be updated by anyone else.

Once the above database transaction is successful, we can start tracking the reservation in 
ActiveReservationService.
"""


def search_movies(api_dev_key, keyword, city, lat_long, radius, start_datetime, end_datetime,
                  postal_code, include_spell_check, results_per_page, sorting_order):
    """
    :param api_dev_key: str:  The API developer key of a registered account. This will be used to, among other things,
    throttle users based on their allocated quota.
    :param keyword: str: Keyword to search on.
    :param city: str: City to filter movies by.
    :param lat_long: str: Latitude and longitude to filter by.
    :param radius: int: Radius of the area in which we want to search for events.
    :param start_datetime: str: Filter movies with a starting datetime.
    :param end_datetime: str: Filter movies with an ending datetime
    :param postal_code: str: Filter movies by postal code / zipcode.
    :param include_spell_check: Enum: Yes, to include spell check suggestions in the response.
    :param results_per_page: int: Number of results to return per page. Maximum is 30.
    :param sorting_order: str: Sorting order of the search result. Some allowable values : ‘name,asc’,
    ‘name,desc’, ‘date,asc’, ‘date,desc’, ‘distance,asc’, ‘name,date,asc’, ‘name,date,desc’,
    ‘date,name,asc’, ‘date,name,desc’.
    :return: JSON [
    {
        "MovieID": 1,
        "ShowID": 1,
        "Title": "Cars 2",
        "Description": "About cars",
        "Duration": 120,
        "Genre": "Animation",
        "Language": "English",
        "ReleaseDate": "8th Oct. 2014",
        "Country": USA,
        "StartTime": "14:00",
        "EndTime": "16:00",
        "Seats":
        [
            {
                "Type": "Regular"
                "Price": 14.99
                "Status: "Almost Full"
            },
            {
                "Type": "Premium"
                "Price": 24.99
                "Status: "Available"
            }
        ]
    },]

    """
    pass


def reserve_seats(api_dev_key, session_id, movie_id, show_id, seats_to_reserve):
    """
    :param api_dev_key: str: The API developer key of a registered account. This will be used to, among other things,
    throttle users based on their allocated quota.
    :param session_id: str: User’s session ID to track this reservation. Once the reservation time
    expires, user’s reservation on the server will be removed using this ID.
    :param movie_id: str: Movie to reserve.
    :param show_id: str: Show to reserve.
    :param seats_to_reserve: list: An array containing seat IDs to reserve.
    :return: JSON: Returns the status of the reservation, which would be one of the following:
    1) “Reservation Successful”
    2) “Reservation Failed - Show Full,”
    3) “Reservation Failed - Retry, as other users are holding reserved seats”.
    """
    pass


class Search(ABC):
    def __init__(self):
        pass

    def search_by_title(self, title):
        pass

    def search_by_language(self, language):
        pass

    def search_by_genre(self, genre):
        pass

    def search_by_release_date(self, rel_date):
        pass

    def search_by_city(self, city_name):
        pass


# Step-11
class Notification:
    """
    Will take care of sending notifications to customers.
    """

    def __init__(self):
        pass


# Step-10
class Payment:
    """
    Responsible for collecting payments from customers.
    """

    def __init__(self, payment_id, amount, timestamp, discount_coupon_id, remote_transaction,
                 payment_method, booking_id):
        pass


# Step-9
class Booking:
    """
    A booking is against a movie show and has attributes like a unique booking number, number of seats,
    and status.
    """

    def __init__(self, booking_id, number_of_seats, timestamp, status, user_id, show_id):
        pass

    def reserve_seats(self, seats):
        pass


# Step-8
class ShowSeat:
    """
    Each ShowSeat will correspond to a movie Show and a CinemaHallSeat. Customers will make a booking
    against a ShowSeat.
    """

    def __init__(self, show_seat_id, status, price, cinema_sheet_id, show_id, booking_id):
        pass

    def is_sheet_available(self):
        pass


# Step-7
class CinemaHallSeat:
    """
    Each cinema hall will have many seats.
    """

    def __init__(self, cinema_sheet_id, seat_number, type, cinema_hall_id):
        pass


# Step-6: The user selects a show.
class Show:
    """
    Each movie can have many shows; each show will be played in a cinema hall.
    """

    def __init__(self, show_id, date, start_time, end_time, cinema_hall_id, movie_id):
        pass

    def is_available_show(self):
        pass

    def select_show(self):
        pass


# Step-5
class Movie:
    """
    The main entity of the system. Movies have attributes like title, description, duration, language,
    genre, release date, city name, etc.
    """

    def __init__(self, movie_id, title, description, duration, language, genre, release_date, city_name):
        self.search_obj = Search()

    def get_shows(self):
        pass


# Step-4
class CinemaHall:
    def __init__(self, cinema_hall_id, name, total_seats, cinema_id):
        pass


# Step-3
class Cinema:
    """
    The main part of the organization for which this software has been designed. It has attributes like
    'name' to distinguish it from other cinemas.
    """

    def __init__(self, cinema_id, name, total_cinema_hall, city_id):
        pass


# Step-2
class City:
    """
    Each city can have multiple cinemas.
    """

    def __init__(self, city_id, name, state, zip_code):
        pass


# Step-1
class User:
    """
    User can search and view movies descriptions.
    """

    def __init__(self, user_id, name, password, email, phone_number):
        """
        :param user_id: int
        :param name: str
        :param password: str
        :param email: str
        :param phone_number: str
        """
