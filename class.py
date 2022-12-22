import csv


class Airport:
    def __init__(self, name: str = None, code: str = None, lat: float = None, longitude: float = None):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = longitude
    def __str__(self):
        return f'{self.name} ({self.code}) - Latitude : {self.lat} / Longitude : {self.long}'

class Flight:
    def __init__(self, departure_code: str = None, arrival_code: str = None, duration: float = None):
        self.departure_code = departure_code
        self.arrival_code = arrival_code
        self.duration = duration
    
    def __str__(self):
        return f'De {self.departure_code} à {self.arrival_code} - Durée : {self.duration} heures'

class FlightMap:

    def __init__(self):
        self.airports_list = []
        self.flights_list = []
        
    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file, quotechar='"', skipinitialspace=True)
            for row in reader:
                name, code, lat, longitude = row
                self.airports_list.append(Airport(name, code, float(lat), float(longitude)))

            
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f, quotechar='"', skipinitialspace=True)
            for row in reader:
                departure_code, arrival_code, duration = row
                self.flights_list.append(Flight(departure_code, arrival_code, float(duration)))

    def airports(self):
        return self.airports_list

    def flights(self):
        return self.flights_list

    def airport_find(self, airport_code: str) -> Airport:
        for i in self.airports_list:
            if i.code == airport_code:
                return i
        return None

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for f in self.flights_list:
            # print('h'+f.arrival_code + dst_airport_code + 'h')
            if f.departure_code == src_airport_code and f.arrival_code == dst_airport_code:
                return True
        return False

    def __str__(self):
        airport_str = 'Aéroports :\n'
        for airport in self.airports:
            airport_str += f' - {airport}\n'
        flight_str = 'Vols :\n'
        for flight in self.flights:
            flight_str += f' - {flight}\n'
        return airport_str + flight_str

flight_map = FlightMap()
flight_map.import_airports('./aeroports.csv')
flight_map.import_flights('./flights.csv')


# airports = flight_map.airports() 
# for i in airports:
#     print(i.code)


# flights = flight_map.flights()  
# print(*map(str, flights))



# airport = flight_map.airport_find('CDG')
# if airport != None:
#     print(f"Aéroport trouvé : {airport}")
# else:
#     print("Aéroport non trouvé")

# print(flight_map.flight_exist('AKL', 'CPT'))
if flight_map.flight_exist('BNE', 'AKL'):
    print("Il existe un vol direct")
else:
    print("Il n'existe pas de vol direct ")



