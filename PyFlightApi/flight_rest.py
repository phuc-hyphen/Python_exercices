#!C:\Apps\Python\Python38 python
# encoding: utf8
import flask
from flask import request, jsonify, Response, make_response
import json
import flights_db
import logging.config
import config, datetime
from random import randrange
from dateutil.relativedelta import relativedelta
from postJIRA import JiraPost

import requests

app = flask.Flask(__name__)

logging.config.fileConfig('logging.conf')
print ("FlightsApp Rest Api")
print ("Listening on http://localhost:5000")
print ("Sample request :  http://localhost:5000/flights_api/v1/resources/Flights/10487")


@app.route('/', methods=['GET'])
def home():
    return '''<h1>FlightsApp Rest Api</h1>
<p>Listening on http://localhost:5000</p>
<p>Sample request :
http://127.0.0.1:5000/flights_api/v1/resources/Flights/?DepartureCity=Paris&ArrivalCity=London&Date=2021-09-03
</p>
'''

#   GET http://localhost:5000/flights_api/v1/resources/Cities?CityName=Paris
@app.route('/flights_api/v1/resources/Cities', methods=['GET'])
def GetCities():
    db = flights_db.sqlite_db()
    city_name = request.args.get('CityName')
    if (city_name is None):
        city_name=''
    cities = db.get_city(city_name)
    json_string = json.dumps([ob.__dict__ for ob in cities])
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# POST  http://localhost:5000/flights_api/v1/resources/Cities
#   {
#     "CityInitials":"CMN",
#     "CityName":"Casablanca"
# }
@app.route('/flights_api/v1/resources/Cities', methods=['POST'])
def CreateCity():
    db = flights_db.sqlite_db()
    if (request.is_json):
        data = request.get_json()
        city = db.create_city(data['CityInitials'], data['CityName'])
    json_string = json.dumps(city.__dict__)
    response = make_response(json_string,201,)
    response.headers["Content-Type"] = "application/json"
    return response

#  PATCH http://localhost:5000/flights_api/v1/resources/Cities/Casablanca
#   {"TicketPrice":185.2}
@app.route('/flights_api/v1/resources/Cities/<CityName>', methods=['PATCH'])
def UpdateCity(CityName):
    db = flights_db.sqlite_db()
    upd_city = db.get_city(CityName)
    if (request.is_json):
        data = request.get_json()
        new_city_initials = data['CityInitials']
        new_city_name = data['CityName']
        upd_city = db.update_city(CityName, new_city_initials, new_city_name)
    json_string = json.dumps(upd_city.__dict__)
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response


# DELETE  http://localhost:5000/flights_api/v1/resources/Cities/Casablanca
@app.route('/flights_api/v1/resources/Cities/<CItyName>', methods=['DELETE'])
def DeleteCity(CItyName):
    db = flights_db.sqlite_db()
    rows = db.delete_city(CItyName)
    if (rows==1):
        json_string = {"true": "City deleted {0} ".format(CItyName)}
    else:
        json_string = {"false": "City not found  {0} ".format(CItyName)}

    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# GET http://localhost:5000/flights_api/v1/resources/RandomFlights?Count=10
@app.route('/flights_api/v1/resources/RandomFlights', methods=['GET'])
def GetRandomFlights():
    random_fligths = []
    cities = flights_db.sqlite_db().get_city('')
    if (request.args.get('Count') is None):
        Count = 10
    else:
        Count = int(request.args.get('Count'))
    for i in range (Count):
        futur = randrange (20) + 30
        date = datetime.date.today()+ relativedelta(days=futur)
        date = date.strftime('%Y-%m-%d')
        DepartureCity = cities[randrange(10)].CityName
        ArrivalCity = DepartureCity
        while (ArrivalCity == DepartureCity):
            ArrivalCity = cities[randrange(10)].CityName
        resp = requests.get(config.url + '/Flights?DepartureCity='+DepartureCity+'&ArrivalCity='+ArrivalCity+'&Date=' + date)
        flights = json.loads(resp.content)
        index = randrange (len(flights))
        flights[index]["Date"] = date
        random_fligths.append (flights[index])

    response = make_response(json.dumps(random_fligths),200,)
    response.headers["Content-Type"] = "application/json"
    return response


#   GET http://localhost:5000/flights_api/v1/resources/Flights?DepartureCity=Paris&ArrivalCity=Denver&Date=2021-12-08
@app.route('/flights_api/v1/resources/Flights', methods=['GET'])
def GetFlights():
    db = flights_db.sqlite_db()
    DepartureCity = request.args.get('DepartureCity')
    ArrivalCity = request.args.get('ArrivalCity')
    FlightDate = request.args.get('Date')
    flights = db.get_flights(DepartureCity, ArrivalCity, FlightDate)
    json_string = ''
    if (flights == -1):
        json_string = jsonify({"error": "Invalid DepartureCity : {0} ".format(DepartureCity)}), 500
    if (flights == -2):
        json_string = jsonify({"error": "Invalid ArrivalCity : {0} ".format(ArrivalCity)}), 500
    else:
        json_string = json.dumps([ob.__dict__ for ob in flights])
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

#   GET http://localhost:5000/flights_api/v1/resources/Flights/16939
@app.route('/flights_api/v1/resources/Flights/<flight_number>', methods=['GET'])
def GetFlightByNumber(flight_number):
    db = flights_db.sqlite_db()
    flight = db.get_flight(flight_number)
    if (flight == -1):
        json_string = {"error": "Unkown Flight  : {0} ".format(flight_number)}
    else:
        json_string = json.dumps(flight.__dict__)
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

#  PATCH http://localhost:5000/flights_api/v1/resources/Flights/16939
#   {"TicketPrice":185.2}
@app.route('/flights_api/v1/resources/Flights/<flight_number>', methods=['PATCH'])
def UpdateFlightPrice(flight_number):
    db = flights_db.sqlite_db()
    upd_fligth = db.get_flight(flight_number)
    if upd_fligth == -1:
        response = make_response({"error":"Unkown flight"}, 200, )
        response.headers["Content-Type"] = "application/json"
        return response

    if (request.is_json):
        data = request.get_json()
        price = data['TicketPrice']
        upd_fligth = db.update_flight_price(flight_number, price)
    json_string = json.dumps(upd_fligth.__dict__)
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# POST  http://localhost:5000/flights_api/v1/resources/Flights
#   {"Airline":"AF", "ArrivalCity":"Casablanca", "ArrivalTime":"10:30 AM", "DepartureCity":"Paris", "DepartureTime":"08:00 AM", "FlightNumber":99558, "Price":185.2, "DayOfWeek":"Monday"}
@app.route('/flights_api/v1/resources/Flights', methods=['POST'])
def CreateFlight():
    print("je suis arrivé!")
    db = flights_db.sqlite_db()
    if (request.is_json):
        data = request.get_json()
        # print(json.dumps(data))
        JiraPost(data)
        
        flight_number = data['FlightNumber']
        flt = db.get_flight(flight_number)
        flt = db.create_flight(flight_number, data['Airline'], data['ArrivalCity'] , data['ArrivalTime'], data['DepartureCity'], data['DepartureTime'], data['Price'], data['DayOfWeek'])
    json_string = json.dumps(flt.__dict__)
    response = make_response(json_string,201,)
    response.headers["Content-Type"] = "application/json"
    return response

# GET  http://localhost:5000/flights_api/v1/resources/FlightOrders?CustomerName=IMHAH
@app.route('/flights_api/v1/resources/FlightOrders', methods=['GET'])
def GetOrders():
    db = flights_db.sqlite_db()
    CustomerName = request.args.get('CustomerName')
    orders = db.get_orders('', CustomerName)
    json_string = json.dumps([ob.__dict__ for ob in orders])
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# GET  http://localhost:5000/flights_api/v1/resources/FlightOrders/81
@app.route('/flights_api/v1/resources/FlightOrders/<OrderNumber>', methods=['GET'])
def GetOrder(OrderNumber):
    db = flights_db.sqlite_db()
    orders = db.get_orders(OrderNumber, '')
    if (len(orders)>0):
        json_string = json.dumps(orders[0].__dict__)
    else:
        json_string = {"error":"invalid order number {0}".format(OrderNumber)}
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# DELETE  http://localhost:5000/flights_api/v1/resources/FlightOrders/81
@app.route('/flights_api/v1/resources/FlightOrders/<OrderNumber>', methods=['DELETE'])
def DeleteOrder(OrderNumber):
    db = flights_db.sqlite_db()
    rows = db.delete_flight_order(OrderNumber)
    if (rows==1):
        json_string = {"true": "Oder deleted {0} ".format(OrderNumber)}
    else:
        json_string = {"false": "Oder not found  {0} ".format(OrderNumber)}
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# DELETE  http://localhost:5000/flights_api/v1/resources/FlightOrders
@app.route('/flights_api/v1/resources/FlightOrders', methods=['DELETE'])
def DeleteAllOrders():
    db = flights_db.sqlite_db()
    orders = db.delete_all_orders();
    json_string = json.dumps([ob.__dict__ for ob in orders])
    response = make_response(json_string,200,)
    response.headers["Content-Type"] = "application/json"
    return response


# POST  http://localhost:5000/flights_api/v1/resources/FlightOrders
#   {   "DepartureDate":"2021-12-08",
#     "FlightNumber":16939,
#     "CustomerName": "IMHAH",
#     "NumberOfTickets":2,
#     "Class":"Economy"
# }
@app.route('/flights_api/v1/resources/FlightOrders', methods=['POST'])
def CreateOrder():
    db = flights_db.sqlite_db()
    if (request.is_json):
        data = request.get_json()
        DepartureDate = data['DepartureDate']
        if (not db.date_in_the_past(DepartureDate)):
            return (jsonify({"error": "Flight date cannot be in the past : {0} ".format(DepartureDate)}), 500)
        json_string=''
        CustomerName = data['CustomerName']
        FlightNumber = data['FlightNumber']
        NumberOfTickets = data['NumberOfTickets']
        FlightClass = data['Class']
        new_order = db.create_flight_order(CustomerName, DepartureDate, FlightNumber, NumberOfTickets, FlightClass)
        if (new_order==-1):
            json_string = jsonify({"error": "Ordered tickets too high : {0} ".format(FlightNumber)})
            response = make_response(json_string, 500, )
            response.headers["Content-Type"] = "application/json"
            return response
        elif (new_order==-2):
            json_string = jsonify({"error": "Unkown Flight  : {0} ".format(FlightNumber)})
            response = make_response(json_string, 500, )
            response.headers["Content-Type"] = "application/json"
            return response
        elif (new_order==-3):
            json_string = jsonify({"error": "No more seats available in flight  : {0} ".format(FlightNumber)})
            response = make_response(json_string, 500, )
            response.headers["Content-Type"] = "application/json"
            return response
        else:
            json_string = json.dumps(new_order.__dict__)
            response = make_response(json_string, 200, )
            response.headers["Content-Type"] = "application/json"
            return response
    else:
        json_string = jsonify({"error": "Invalid json format  "})
        response = make_response(json_string,500,)
        response.headers["Content-Type"] = "application/json"
        return response

#   PATCH http://localhost:5000/flights_api/v1/resources/FlightOrders/81
# {   "DepartureDate":"2021-12-08",
#     "FlightNumber":16939,
#     "CustomerName": "IMHAH",
#     "NumberOfTickets":2,
#     "Class":"Economy"
# }
@app.route('/flights_api/v1/resources/FlightOrders/<OrderNumber>', methods=['PATCH'])
def UpdateOrder(OrderNumber):
    db = flights_db.sqlite_db()
    if (request.is_json):
        data = request.get_json()
        DepartureDate = data['DepartureDate']
        if (not db.date_in_the_past(DepartureDate)):
            return (jsonify({"error": "Flight date cannot be in the past : {0} ".format(DepartureDate)}), 500)
        CustomerName = data['CustomerName']
        FlightNumber = data['FlightNumber']
        NumberOfTickets = data['NumberOfTickets']
        FlightClass = data['Class']
        upd_order = db.update_flight_order(OrderNumber, FlightNumber, FlightClass, CustomerName, NumberOfTickets)
        if (upd_order==-1):
            return (jsonify({"error": "Ordered tickets too high : {0} ".format(FlightNumber)}), 500)
        elif (upd_order==-2):
            return (jsonify({"error": "Unkown Flight  : {0} ".format(FlightNumber)}), 500)
        elif (upd_order==-3):
            return (jsonify({"error": "No more seats available in flight  : {0} ".format(FlightNumber)}), 500)
        else:
            json_string = json.dumps(upd_order.__dict__)
            response = make_response(json_string, 200, )
            response.headers["Content-Type"] = "application/json"
            return response
    else:
        return (jsonify({"error": "Invalid json format  "}), 500)

app.run()

