from airport import Airport
from flight import Flight
from flightmap import FlightMap
from exception.flightpathbroken import FlightPathBroken
from exception.flightpathduplicate import FlightPathDuplicate


class FlightPath:
    def __init__(self, src_airport: Airport) -> None:

        self.airports_l = [src_airport]
        self.flights_l = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if via_flight == None or self.airports_l[-1] == None:
            raise FlightPathBroken("Entrer invalide")
        if via_flight.src_code != self.airports_l[-1].code:
            raise FlightPathBroken(
                "Le vol ne part pas de l'aéroport de départ")
        if via_flight.dst_code != dst_airport.code:
            raise FlightPathBroken(
                "Le vol n'arrive pas à l'aéroport de destination")
        if via_flight in self.flights_l:
            raise FlightPathDuplicate("Le vol est déjà présent dans le chemin")
        self.flights_l.append(via_flight)
        self.airports_l.append(dst_airport)

    def flights(self) -> list[Flight]:
        return self.flights_l

    def airports(self) -> list[Airport]:
        return self.airports_l

    def steps(self) -> float:
        return len(self.flights_l)

    def duration(self) -> float:
        return sum(flight.duration for flight in self.flights_l)

    def __str__(self) -> str:
        flights_str = '\n'.join([str(flight) for flight in self.flights_l])
        return f"Flights:\n{flights_str}\nTotal steps: {self.steps()}\nTotal duration: {self.duration()}"


# def test_flight_path():
#     flight_map = FlightMap()
#     flight_map.import_flights('./doc/flights.csv')
#     flight_map.import_airports('./doc/aeroports.csv')

#     src_airport = flight_map.airport_find_path('CDG')

#     path = FlightPath(src_airport)

#     dst_airport = flight_map.airport_find_path('HHH')

#     via_flight = flight_map.flight_exist(src_airport.code, dst_airport.code)

#     path.add(dst_airport, via_flight)

#     print(path)


# test_flight_path()

def test_flight_path():
    # Création de l'objet FlightMap et importation des vols et des aéroports à partir de fichiers CSV
    flight_map = FlightMap()
    flight_map.import_flights('./doc/flights.csv')
    flight_map.import_airports('./doc/aeroports.csv')

    # Récupération de l'aéroport de départ
    src_airport = flight_map.airport_find('CDG')

    # Création de l'objet FlightPath
    path = FlightPath(src_airport)

    # Récupération de l'aéroport de destination
    dst_airport = flight_map.airport_find('AMS')

    # Récupération du vol qui relie src_airport et dst_airport
    via_flight = flight_map.flight_exist(src_airport.code, dst_airport.code)

    # Ajout du vol au chemin
    path.add(dst_airport, via_flight)

    # Vérification que le chemin contient bien l'aéroport de départ et l'aéroport de destination
    assert src_airport in path.airports()
    assert dst_airport in path.airports()

    # Vérification que le chemin contient bien le vol qui relie src_airport et dst_airport
    assert via_flight in path.flights()

    # Vérification que la méthode steps renvoie bien le nombre d'étapes du chemin (ici 1)
    assert path.steps() == 1

    # Vérification que la méthode duration renvoie bien la durée totale du chemin (ici la durée du vol via_flight)
    assert path.duration() == via_flight.duration


# Appel de la fonction de test
test_flight_path()
