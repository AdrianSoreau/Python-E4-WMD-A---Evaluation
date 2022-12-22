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

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for f in self.flights_list:
            # print('h'+f.arrival_code + dst_airport_code + 'h')
            if f.departure_code == src_airport_code and f.arrival_code == dst_airport_code:
                return True
        return False

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


class FlightPathBroken(Exception):
    pass


class FlightPathDuplicate(Exception):
    pass


class FlightPath():


    def __init__(self, src_airport: Airport) -> None:
            # Initialise la liste d'aéroports avec l'aéroport de départ
        self.airports_list = [src_airport]
# Initialise la liste de vols vide
        self.flights_list = []


    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
    # Vérifie que le vol via_flight passe par l'aéroport de départ du chemin
        if self.airports_list[-1].code != via_flight.departure_code:
            raise FlightPathBroken(
                'Le vol {} ne passe pas par l\'aéroport de départ du chemin'.format(via_flight))
    # Vérifie que l'aéroport de destination n'a pas déjà été ajouté au chemin
        if dst_airport in self.airports_list:
            raise FlightPathDuplicate(
                'L\'aéroport de destination {} a déjà été ajouté au chemin'.format(dst_airport))
    # Ajoute l'aéroport de destination à la liste des aéroports
        self.airports_list.append(dst_airport)
    # Ajoute le vol à la liste des vols
        self.flights_list.append(via_flight)


    def flights(self) -> list[Flight]:
        return self.flights_list


    def airports(self) -> list[Airport]:
        return self.airports_list


    def steps(self) -> float:
        return len(self.flights_list)


    def duration(self) -> float:
        return sum([flight.duration for flight in self.flights_list])


def test_flight_path():
    # Création d'un aéroport de départ
    src_airport = Airport(name='Paris Charles de Gaulle Airport',
        code='CDG', lat=49.012779, longitude=2.55)

    # Initialisation d'un objet FlightPath avec l'aéroport de départ
    path = FlightPath(src_airport)

    # Vérification que la méthode airports retourne une liste avec un élément (l'aéroport de départ)
    assert path.airports() == [src_airport]

    # Vérification que la méthode flights retourne une liste vide (pas encore de vols dans le chemin)
    assert path.flights() == []

    # Vérification que la méthode steps retourne 0 (pas encore de vols dans le chemin)
    assert path.steps() == 0

    # Vérification que la méthode duration retourne 0 (pas encore de vols dans le chemin)
    assert path.duration() == 0


def test_init():

    src_airport = Airport(name='Paris Charles de Gaulle Airport',
        code='CDG', lat=49.012779, longitude=2.55)

    path = FlightPath(src_airport)

    assert path.src_airport == src_airport

test_init()
