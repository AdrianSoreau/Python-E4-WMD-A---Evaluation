import csv
from airport import Airport
from flight import Flight
from aeorportnotfind import AeroNotFound
class FlightMap:

    def __init__(self):
        self.airports_list = []
        self.flights_list = []

    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file, quotechar='"', skipinitialspace=True)
            for row in reader:
                name, code, lat, longitude = row
                self.airports_list.append(
                    Airport(name, code, float(lat), float(longitude)))

    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f, quotechar='"', skipinitialspace=True)
            for row in reader:
                departure_code, arrival_code, duration = row
                self.flights_list.append(
                    Flight(departure_code, arrival_code, float(duration)))

    def airports(self):
        return self.airports_list

    def flights(self):
        return self.flights_list

    def airport_find(self, airport_code: str) -> Airport:
        for i in self.airports_list:
            if i.code == airport_code:
                return i
        
        return None

    def airport_find_path(self, airport_code: str) -> Airport:
        for i in self.airports_list:
            if i.code == airport_code:
                return i
            
        raise AeroNotFound("L'aéroport n'a pas été trouvé")

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for f in self.flights_list:
            # print('h'+f.arrival_code + dst_airport_code + 'h')
            if f.departure_code == src_airport_code and f.arrival_code == dst_airport_code:
                return f
        return None

    def flights_where(self, airport_code: str) -> list[Flight]:
        flights = []
        for flight in self.flights_list:
            if flight.departure_code == airport_code or flight.arrival_code == airport_code:
                flights.append(flight)
        return flights

    def airports_from(self, airport_code: str) -> list[Airport]:
        airports = []
        for flight in self.flights_where(airport_code):
            if flight.departure_code == airport_code:
                airport = self.airport_find(flight.arrival_code)
                if airport:
                    airports.append(airport)
        return airports

    def __str__(self):
        airport_str = 'Aéroports :\n'
        for airport in self.airports:
            airport_str += f' - {airport}\n'
        flight_str = 'Vols :\n'
        for flight in self.flights:
            flight_str += f' - {flight}\n'
        return airport_str + flight_str
