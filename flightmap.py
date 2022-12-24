import csv
from airport import Airport
from flight import Flight
from exception.aeorportnotfind import AeroNotFound


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
                src_code, dst_code, duration = row
                self.flights_list.append(
                    Flight(src_code, dst_code, float(duration)))

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
            # print('h'+f.dst_code + dst_airport_code + 'h')
            if f.src_code == src_airport_code and f.dst_code == dst_airport_code:
                return f
        return None

    def flights_where(self, airport_code: str) -> list[Flight]:
        flights = []
        for flight in self.flights_list:
            if flight.src_code == airport_code or flight.dst_code == airport_code:
                flights.append(flight)
        return flights

    def airports_from(self, airport_code: str) -> list[Airport]:
        airports = []
        for flight in self.flights_where(airport_code):
            if flight.src_code == airport_code:
                airport = self.airport_find(flight.dst_code)
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


def test_flight_map():
    flight_map = FlightMap()
    flight_map.import_flights("./doc/flights.csv")
    flight_map.import_airports("./doc/aeroports.csv")
    print("Aéroports :")
    for airport in flight_map.airports():
        print(f" - {airport}")
    print("Vols :")
    for flight in flight_map.flights():
        print(f" - {flight}")
    print("Recherche de l'aéroport CDG :")
    print(flight_map.airport_find("CDG"))
    print("Vols partant de CDG :")
    for flight in flight_map.flights_where("CDG"):
        print(f" - {flight}")
    print("Aéroports accessibles depuis CDG :")
    for airport in flight_map.airports_from("CDG"):
        print(f" - {airport}")

# test_flight_map()

