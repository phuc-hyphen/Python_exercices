import flights_db
from datetime import datetime, timedelta
from random import randrange


db = flights_db.sqlite_db()
cities = db.get_city('')

print("Departure;Arrival;Date;FlightNumber;Price;SeatsAvailable")

for i in range(20):
    flight_date = str(datetime.now() + timedelta(randrange(15) + 21))[0:10]
    departure_city = cities[randrange(10)].CityName
    arrival_city = departure_city
    while (arrival_city == departure_city):
        arrival_city = cities[randrange(10)].CityName
    flights = db.get_flights(departure_city, arrival_city, flight_date)
    random_flight = flights[randrange(len(flights))]
    print(departure_city+';'+arrival_city+';'+flight_date+';'+str(random_flight.FlightNumber)+';'+str(random_flight.Price)+';'+str(random_flight.SeatsAvailable))

db.close_db()