from airport import Airport
from flight import Flight
from flightmap import FlightMap
from flightpathbroken import FlightPathBroken
from flightpathduplicate import FlightPathDuplicate


class FlightPath:
    def __init__(self, src_airport: Airport) -> None:

        self.airports_l = [src_airport]
        self.flights_l = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if via_flight == None or self.airports_l[-1] == None:
            raise FlightPathBroken("Entrer invalide")
        if via_flight.departure_code != self.airports_l[-1].code:
            raise FlightPathBroken(
                "Le vol ne part pas de l'aéroport de départ du chemin")
        if via_flight.arrival_code != dst_airport.code:
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



def test_flight_path() :
    flight_map = FlightMap()
    flight_map.import_flights('./flights.csv')
    flight_map.import_airports('./aeroports.csv')

    src_airport = flight_map.airport_find_path('CDG')

    path = FlightPath(src_airport)

    dst_airport = flight_map.airport_find_path('HHH')

    via_flight = flight_map.flight_exist(src_airport.code, dst_airport.code)

    path.add(dst_airport, via_flight)

    print(path)

test_flight_path()
