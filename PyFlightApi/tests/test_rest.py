# -*- coding: utf-8 -*-
# Illustration du fonctionnement de unitest et difference entre setUp et setUpClass, tearDown et tearDownClass
import unittest
import logging
import requests, json
import config
from random import randrange


class test_rest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filename='test_soap.log', filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s')
        cls.date = '2021-12-21'
        cls.flight = 10487
        cls.order=0

    @unittest.skip
    def test_a_GetCities(self):
        resp = requests.get (config.url + '/Cities')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(len(data), 10)
    @unittest.skip
    def test_b_GetCity(self):
        resp = requests.get (config.url + '/Cities?CityName=Paris')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data[0]['CityInitials'], 'PAR')
        self.assertEqual(data[0]['CityName'], 'Paris')

    @unittest.skip
    def test_c_CreateCity(self):
        header = {"content-type":"application/json"}
        city = {"CityInitials":"CMN","CityName":"Casablanca"}
        resp = requests.post (config.url + '/Cities', data=json.dumps(city), headers=header)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['CityInitials'], 'CMN')
        self.assertEqual(data['CityName'], 'Casablanca')

    @unittest.skip
    def test_d_UpdateCity(self):
        header = {"content-type":"application/json"}
        city = {"CityInitials":"CASA","CityName":"Anfa"}
        resp = requests.patch (config.url + '/Cities/Casablanca', data=json.dumps(city), headers=header)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['CityInitials'], 'CASA')
        self.assertEqual(data['CityName'], 'Anfa')

    @unittest.skip
    def test_e_DeleteCity(self):
        header = {"content-type":"application/json"}
        resp = requests.delete (config.url + '/Cities/Anfa')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertIn('City deleted', data['true'])

    @unittest.skip
    def test_a_GetFlights(self):
        resp = requests.get (config.url + '/Flights?DepartureCity=Paris&ArrivalCity=London&Date='+ self.date)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.__class__.flight = data[0]['FlightNumber'];
        print (self.__class__.flight)

    @unittest.skip
    def test_a_GetFlights_fail(self):
        resp = requests.get (config.url + '/Flights?DepartureCity=Casablanca&ArrivalCity=London&Date='+ self.date)
        self.assertEqual(resp.status_code, 500)

    @unittest.skip
    def test_a_GetFlights_date(self):
        resp = requests.get (config.url + '/Flights?DepartureCity=&ArrivalCity=&Date='+ self.date)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        for i in range(20):
            random_flight = data[randrange(len(data))]
            print(random_flight['DepartureCity'], random_flight['ArrivalCity'], random_flight['FlightNumber'], self.date)

    @unittest.skip
    def test_a_CreateFlight(self):
        print (config.url + '/Flights')
        header = {"content-type":"application/json"}
        flt = {'Airline':'AF', 'ArrivalCity':'Casablanca', 'ArrivalTime':'10:30 AM', 'DepartureCity':'Paris', 'DepartureTime':'08:00 AM', 'FlightNumber':356982365, 'Price':185.2, 'DayOfWeek':'Monday'}
        resp = requests.post (config.url + '/Flights', data=json.dumps(flt), headers=header)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.__class__.flight = 356982365
        print (data)
        resp = requests.get (config.url + '/Flights?DepartureCity=Paris&ArrivalCity=Casablanca&Date=2021-11-01')
        self.assertEqual(resp.status_code, 500)
        data = json.loads(resp.content)

    @unittest.skip
    def test_b_GetUnknownFlight(self):
        print (config.url + '/Flights/9999999' )
        resp = requests.get (config.url + '/Flights/9999999')
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.content)
        print (data)

    # @unittest.skip
    def test_b_GetFlight(self):
        print(config.url + '/Flights/'+ str(self.__class__.flight))
        resp = requests.get (config.url + '/Flights/'+ str(self.__class__.flight))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        print (data)

    @unittest.skip
    def test_e_UpdateFligthPrice(self):
        header = {"content-type":"application/json"}
        data = {"TicketPrice":185.2}
        resp = requests.patch (config.url + '/Flights/'+ str(self.__class__.flight), data=json.dumps(data), headers=header)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        print(data)

    @unittest.skip
    def test_c_CreateOrder(self):
        header = {"content-type":"application/json"}
        data = {"DepartureDate":self.date, "FlightNumber":self.__class__.flight,"CustomerName":"IMHAH","NumberOfTickets":"2", "Class":"Economy"}
        print(config.url + '/FlightOrders')
        print(data)
        resp = requests.post (config.url + '/FlightOrders', data=json.dumps(data), headers=header)
        self.assertEqual(resp.status_code, 201)
        data = json.loads(resp.content)
        print (data)
        self.__class__.order = data['OrderNumber']

    @unittest.skip
    def test_d_GetOrdersByCustomerName(self):
        print (config.url + '/FlightOrders?CustomerName=IMHAH&OrderNumber=' + str(self.__class__.order))
        resp = requests.get (config.url + '/FlightOrders?CustomerName=IMHAH&OrderNumber=' + str(self.__class__.order))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        print(data)

    @unittest.skip
    def test_d_GetAllOrders(self):
        print (config.url+ '/FlightOrders')
        resp = requests.get (config.url+ '/FlightOrders')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        print(data)

    @unittest.skip
    def test_e_UpdateOrder(self):
        header = {"content-type":"application/json"}
        data = {"DepartureDate":self.date, "FlightNumber":self.__class__.flight,"CustomerName":"IMHAH","NumberOfTickets":"2", "Class":"First"}
        resp = requests.patch (config.url + '/FlightOrders/'+ str(self.__class__.order), data=json.dumps(data), headers=header)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        print(data)

    @unittest.skip
    def test_f_GetOrdersByOrderNumber(self):
        resp = requests.get(config.url + '/FlightOrders?OrderNumber=' + str(self.__class__.order ))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        print(data)

    @unittest.skip
    def test_z_DeleteFlightOrder(self):
        print(str(self.__class__.order ))
        resp = requests.delete(config.url + '/FlightOrders/' + str(self.__class__.order ))
        self.assertEqual(resp.status_code, 200)

    @unittest.skip
    def test_z_generate_random_fligth(self):
        resp = requests.get(config.url + '/RandomFlights?Count=15')
        self.assertEqual(resp.status_code, 200)
        flights = json.loads(resp.content)
        print("Arrival,Departure,Date,FlightNumber,Price")
        for flt in flights:
            print (flt["ArrivalCity"]+','+flt["DepartureCity"] +','+flt["Date"] +','+ str(flt["FlightNumber"])+','+str(flt["Price"]))
