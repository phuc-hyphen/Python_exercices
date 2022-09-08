import sys
import traceback
import sqlite3 as sl
from spyne.model.complex import ComplexModel
from spyne.model.primitive import Integer
from spyne.model.primitive import String
from spyne.model.primitive import Float
from datetime import date
from datetime import datetime
import calendar
import logging
import config
from datetime import datetime, timedelta
from os.path import abspath

logger = logging.getLogger(__name__)

class Flight(ComplexModel):
    __namespace__ = 'Flight'
    Airline = String
    ArrivalCity = String
    ArrivalTime = String
    DepartureCity = String
    DepartureTime = String
    FlightNumber = Integer
    Price = Float
    SeatsAvailable = Integer

class FlightOrder(ComplexModel):
   __namespace__ = 'FlightOrder'
   Class = String
   CustomerName = String
   DepartureDate = String
   FlightNumber = Integer
   NumberOfTickets = Integer
   OrderNumber = Integer
   TotalPrice = Float

class Order(ComplexModel):
   __namespace__ = 'Order'
   OrderNumber = Integer
   TotalPrice = Float

class City(ComplexModel):
   __namespace__ = 'City'
   CityInitials = String
   CityName = String

class   sqlite_db ():
    __namespace__ = 'sqlite_db'
    def __init__(self):
        logging.info (abspath(config.flight_db))
        self.con = sl.connect(abspath(config.flight_db))
        logging.info (self.con)
    def close_db(self):
        self.con.close()


    def log_sql_error (self, err):
        logging.error('SQLite error: %s' % (' '.join(err.args)))
        logging.error("Exception class is: ", err.__class__)
        logging.error('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        logging.error(traceback.format_exception(exc_type, exc_value, exc_tb))

    #
    # Utils
    #
    # Get day name from date
    def get_week_day(self, year, month, day):
        dt = date(year, month, day)
        return (calendar.day_name[dt.weekday()])
    # Convert Flight Class number to name 1 - Business, 2-First, 3-Economy
    def flight_class_name (self, flght_class):
        flght_class_name = 'N/A'
        if flght_class == 1:
            flght_class_name = 'Business'
        elif flght_class == 2:
            flght_class_name = 'First'
        elif flght_class == 3:
            flght_class_name = 'Economy'
        return (flght_class_name)
    # Check if date is in the past
    def date_in_the_past(self, flight_date):
        flight_date = datetime.strptime(flight_date, "%Y-%m-%d")
        return(flight_date > datetime.now())
    # Convert Flight Class name  to Number  1 - Business, 2-First, 3-Economy
    def flight_class_numer(self, flght_class_name):
        flight_class = 0
        if flght_class_name == 'Business':
            flight_class = 1
        elif flght_class_name == 'First':
            flight_class = 2
        elif flght_class_name == 'Economy':
            flight_class = 3
        return (flight_class)
    # Convert date + time (AM/PM) to datetime 24h
    def get_flight_datetime (self, departure_date, departure_time):
        time_parts = departure_time.split(' ')[0].split(':')
        date_parts = departure_date.split('-')
        hour = time_parts[0]
        if (departure_time.split(' ')[1] == 'PM'):
            hour = str(int(hour) + 12)
        return (date_parts[0] + '-' + str(int(date_parts[1])) + '-' +  str(int(date_parts[2])) + ' ' +  str(hour) +':' +  time_parts[1])
    #
    # Cities
    #
    def get_city (self, city_name):
        cities = []
        sql = 'SELECT c.CityInitials, c.CityName FROM Cities c WHERE c.CityName like \'%' + city_name + '%\';'
        logging.info ('city_exists %s : ', city_name)
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            res = cur.execute(sql)
            for r in res:
                city = City ()
                city.CityInitials = r[0]
                city.CityName = r[1]
                cities.append(city)
        return (cities)
    def city_exists (self, city_name):
        cities = self.get_city (city_name)
        return (len(cities)>0)
    def create_city (self, city_initials, city_name):
        cities = self.get_city(city_name)
        city = City()
        if (len(cities)>0):
            return (cities [0])
        sql = 'INSERT INTO Cities (CityInitials, CityName) values (?, ?)'
        data = (city_initials, city_name)
        with self.con:
            try:
                self.con.execute(sql, data)
                city.CityInitials = city_initials
                city.CityName = city_name
            except sl.con.Error as err:
                self.log_sql_error (err)
        return (city)
    def update_city (self, city_name, new_city_initials, new_city_name):
        cities =  self.get_city(city_name)
        if (len(cities)==0):
            return 0
        sql = 'UPDATE Cities SET CityInitials = \''+ new_city_initials + '\''
        sql += ', CityName = \'' + new_city_name + "'"
        sql += ' WHERE CityName=\'' + str(city_name) + '\''
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql)
        return (self.get_city(new_city_name)[0])
    def delete_city (self, city_name):
        cities = self.get_city (city_name)
        if (len(cities) == 0):
            return 0
        sql = 'DELETE FROM  Cities  WHERE CityName=\'' + city_name +'\''
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql)
            row_deleted = cur.rowcount
        return (row_deleted)
    #
    # Flights
    #
    def create_flight (self, flight_number, airline, arrival, arrival_time, departure, departure_time , ticket_price, day_of_week):
        flight = self.get_flight(flight_number)
        if (flight == -1):
            sql = 'INSERT INTO Flights (Airline, Arrival, ArrivalTime, Departure, DepartureTime , FlightNumber , TicketPrice, SeatsAvailable, DayOfWeek) values(?, ?, ?, ?, ?, ?, ?, ?, ?)'
            data = (airline, arrival, arrival_time, departure, departure_time, flight_number, ticket_price, 250, day_of_week)
            with self.con:
                try:
                    self.con.execute(sql, data)
                except sl.con.Error as err:
                    self.log_sql_error (err)
            return (self.get_flight(flight_number))
        else:
            return(flight)
    def get_flights (self, departure_city, arrival_city, flight_date):
        logging.info ('get_flights departure_city : %s - arrival_city : %s - flight_date : %s ', departure_city, arrival_city, flight_date)
        flights = []
        day_name = ''
        if (not self.city_exists(departure_city)):
            return -1

        if (not self.city_exists(arrival_city)):
            return -2

        if (flight_date.find('-') > 0):
            date_parts = flight_date.split('-')
            day_name = self.get_week_day (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
        sql = 'SELECT 	f.Airline , f.Arrival , f.ArrivalTime, f.Departure,f.DepartureTime , f.FlightNumber , f.TicketPrice, f.SeatsAvailable, f.DayOfWeek FROM 	Flights f  '
        criterias = ''
        if (len(departure_city) > 0):
            criterias += ' f.Departure = \'' + departure_city + '\' '

        if (len(arrival_city) > 0):
            if (len(criterias) > 0):
                criterias += ' AND '
            criterias += ' f.Arrival = \'' + arrival_city + '\' '

        if (len(day_name) > 0):
            if (len(criterias) > 0):
                criterias += ' AND '
            criterias += ' f.DayOfWeek = \'' + day_name + '\' '

        if (len(criterias) > 0):
            sql = sql + ' WHERE ' + criterias

        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            res = cur.execute(sql)
            for r in res:
                flight = Flight()
                flight.Airline = r[0]
                flight.ArrivalCity = r[1]
                flight.ArrivalTime = r[2]
                flight.DepartureCity = r[3]
                flight.DepartureTime = r[4]
                flight.FlightNumber = r[5]
                flight.Price = r[6]
                flight.SeatsAvailable = r[7]
                flight.DayOfWeek = r[8]
                flights.append( flight )
        return (flights)
    def get_flight (self, flight_number):
        logging.info ('get_flight flight_number : %s  ', flight_number)
        sql = 'SELECT 	f.Airline , f.Arrival , f.ArrivalTime, f.Departure,f.DepartureTime , f.FlightNumber , f.TicketPrice, f.SeatsAvailable, f.DayOfWeek FROM 	Flights f  '
        sql += ' WHERE f.FlightNumber  = ' + str(flight_number) + ';'
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            if (not row is None):
                flight = Flight()
                flight.Airline = row[0]
                flight.ArrivalCity = row[1]
                flight.ArrivalTime = row[2]
                flight.DepartureCity = row[3]
                flight.DepartureTime = row[4]
                flight.FlightNumber = row[5]
                flight.Price = row[6]
                flight.SeatsAvailable = row[7]
                flight.DayOfWeek = row[8]
            else:
                flight=-1
        return (flight)
    def get_seats_available (self, flight_number):
        sql = 'Select SeatsAvailable from Flights Where FlightNumber = ' + str(flight_number) + ';'
        logging.info(sql)
        cursor = self.con.cursor()
        cursor.execute(sql)
        seats = cursor.fetchone()[0]
        return (seats)
    def update_seats_available (self, flight_number, seats):
        if (seats > 0):
            seats = '+' + str (seats)
        elif (seats < 0):
            seats =  str (seats)
        elif (seats == 0):
            seats=''
        sql = 'UPDATE Flights SET SeatsAvailable =  SeatsAvailable ' + seats + ' WHERE FlightNumber =' + str(flight_number) + ';'
        logging.info(sql)
        self.con.execute(sql)
    def update_all_seats_available (self):
        sql = 'UPDATE Flights SET SeatsAvailable = 250 ;'
        logging.info(sql)
        self.con.execute(sql)
    def update_flight_price (self, flight_number, price):
        flt = self.get_flight(flight_number)
        if (flt.Price != price):
            sql = 'UPDATE Flights SET TicketPrice =  ' + str(price) + ' WHERE FlightNumber =' + str(flight_number) + ';'
            logging.info(sql)
            self.con.execute(sql)
            sql = 'INSERT INTO Audit (tableName, tableColumn, kayName, kayValue, oldValue, newValue, updateDate) values(?, ?, ?, ?, ?, ?, ?)'
            data = ('Flights', 'TicketPrice', 'FlightNumber', str(flight_number), flt.Price, price, datetime.now() )
            self.con.execute(sql, data)
            flt.Price = price
        return (flt)

    #
    # Orders
    #
    def get_orders (self, order_number, customer_name):
        orders = []
        if order_number is None or len(order_number)==0:
            order_number=0
        try:
            order_number = int(order_number)
        except:
            return (orders)
        if customer_name is None:
            customer_name=''
        sql = 'SELECT 	o.OrderNumber , o.CustomerName , o.DepartureDate, o.FlightNumber , o.TicketsOrdered , o.Class, o.TotalPrice FROM	Orders o'
        criteria = ''
        if (order_number!=0):
            criteria = ' o.OrderNumber =  '  + str(order_number)
        if (customer_name != ''):
            if (len(criteria) > 0):
                criteria += ' AND o.CustomerName =  \'' + customer_name + '\''
            else:
                criteria += ' o.CustomerName =  \'' + customer_name + '\''

        if (len(criteria)>0):
            criteria = ' WHERE ' + criteria
        sql = sql + criteria + ';'
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            res = cur.execute(sql)
            for r in res:
                flight_class = self.flight_class_name (r[5])
                order = FlightOrder()
                order.Class = flight_class
                order.Class = flight_class
                order.CustomerName = r[1]
                order.DepartureDate = r[2]
                order.FlightNumber = r[3]
                order.NumberOfTickets = r[4]
                order.TotalPrice = r[6]
                order.OrderNumber = r[0]
                orders.append (order)
        return (orders)
    def create_flight_order (self, customer_name, departure_date, flight_number, tickets_ordered, flight_class):
        flight = self.get_flight(flight_number)
        if (flight==-1):
            return (-4)
        total_price = flight.Price * float(tickets_ordered)
        if (flight.FlightNumber is None):
            return(-2)
        seats_availabe = flight.SeatsAvailable
        if (seats_availabe <= 0):
            return(-3)
        if (int(tickets_ordered) > seats_availabe):
            return (-1)
        last_id = 0
        #  departure_date = get_flight_datetime('2021-02-05', flight.DepartureTime)
        departure_date = self.get_flight_datetime(departure_date, flight.DepartureTime)
        sql = 'INSERT INTO Orders (CustomerName, DepartureDate, FlightNumber, TicketsOrdered, Class, TotalPrice) values(?, ?, ?, ?, ?, ?)'
        data = (customer_name, departure_date, flight_number, tickets_ordered, self.flight_class_numer(flight_class), total_price)
        with self.con:
            self.con.execute(sql, data)
            cursor = self.con.cursor()
            cursor.execute('select last_insert_rowid();')
            last_id = cursor.fetchone()[0]
            self.update_seats_available(flight_number, -1*int(tickets_ordered))
        new_order = Order()
        new_order.OrderNumber = last_id
        new_order.TotalPrice = total_price
        return (new_order)
    def update_flight_order (self, order_number, flight_number, flight_class, customer_name, number_of_tickets):
        orders =  self.get_orders (str(order_number), '')
        if (len(orders)==0):
            return 0
        tickets_ordered_old = orders[0].NumberOfTickets
        class_numer = self.flight_class_numer(flight_class)
        if (class_numer==0):
            return (-1)
        sql = 'UPDATE Orders SET Class = '+ str(class_numer)
        sql += ', CustomerName = \''+customer_name + "'"
        sql += ', FlightNumber = ' + str(flight_number)
        sql += ', TicketsOrdered = '+str(number_of_tickets)
        sql += ' WHERE OrderNumber=' + str(order_number)
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql)
            self.update_seats_available(flight_number, tickets_ordered_old)
            self.update_seats_available(flight_number, -1 * int(number_of_tickets))
        return (self.get_orders(order_number, '')[0])
    def delete_flight_order (self, order_number):
        orders = self.get_orders (order_number, '')
        if (len(orders) == 0):
            return 0
        tickets_ordered = orders[0].NumberOfTickets
        flight_number= orders[0].FlightNumber
        sql = 'DELETE FROM  Orders WHERE OrderNumber=' + str(order_number)
        logging.info (sql)
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql)
            row_deleted = cur.rowcount
            self.update_seats_available(flight_number, tickets_ordered)
        return (row_deleted)
    def delete_all_orders (self):
        logging.info ("Delete all")
        orders = self.get_orders('','')
        with self.con:
            cur = self.con.cursor()
            try:
                cur.execute("DELETE FROM  Orders WHERE OrderNumber > 86;")
                cur.execute('UPDATE sqlite_sequence  SET seq = 86 WHERE name="Orders";')
                cur.execute('Update Flights Set SeatsAvailable = 250;')
            except:
                logging.error("Delete all")
        return (orders)

if __name__ == '__main__':
    sl = sqlite_db()
    '''
    print (sl.get_flight_datetime('2021-12-21', '8:00 AM'))
    print (sl.get_flight_datetime('2021-12-21', '8:00 PM'))
    print (sl.con)
    print (sl.city_exists ('Paris'))
    print (sl.city_exists ('Denver'))
    print (sl.get_flights ('Paris', 'London', '2021-12-25'))
    print (sl.get_flights ('Paris', 'Denver', '2021-12-25'))
'''

    print(sl.delete_city('Casablanca'))

    print(sl.delete_city('Anfa'))

    print (sl.update_flight_price ('10454', 163.4))
    # sl.delete_city('Casablanca')
    print(sl.create_city('CMN', 'Casablanca'))
    print (sl.update_city('Casablanca', 'CASA', 'Anfa'))
    print(sl.get_city('Casablanca'))
    print(sl.get_city(''))
    print(sl.delete_city('Anfa'))
    print(sl.delete_city('Casablanca'))
    # sl.create_flight(5896478523, 'AF', 'Casablanca' , '10:30 AM', 'Paris', '08:00 AM', 185.2, 'Monday')
    # print (sl.get_flight (5896478523))

    '''
    print (sl.create_flight_order ('IMHAH',  '2021-12-25', 10454, 2, 'Economy'))
    print (sl.get_orders('', 'IMHAH'))
    print (sl.get_orders('81', ''))
    print (sl.update_flight_order('81', 'First', 'IMHAH', 5))
    print(sl.get_orders('81', ''))
    '''
    #print(sl.delete_flight_order('81'))
    #print(sl.delete_all_orders())
    sl.close_db()
