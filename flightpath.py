from airport import Airport
from flight import Flight
from flightpathbroken import FlightPathBroken
from flightpathduplicate import FlightPathDuplicate
class FlightPath():

    def __init__(self, src_airport: Airport) -> None:
        self.airports_list = [src_airport]
        self.flights_list = []

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if self.airports_list[-1].code != via_flight.departure_code:
            raise FlightPathBroken(
                'Le vol {} ne passe pas par l\'aéroport de départ du chemin'.format(via_flight))
        if dst_airport in self.airports_list:
            raise FlightPathDuplicate(
                'L\'aéroport de destination {} a déjà été ajouté au chemin'.format(dst_airport))
        self.airports_list.append(dst_airport)
        self.flights_list.append(via_flight)

    def flights(self) -> list[Flight]:
        return self.flights_list

    def airports(self) -> list[Airport]:
        return self.airports_list

    def steps(self) -> float:
        return len(self.flights_list)

    def duration(self) -> float:
        return sum([flight.duration for flight in self.flights_list])
