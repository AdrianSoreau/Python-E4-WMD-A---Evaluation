class Flight:
    def __init__(self, departure_code: str = None, arrival_code: str = None, duration: float = None):
        self.departure_code = departure_code
        self.arrival_code = arrival_code
        self.duration = duration

    def __str__(self):
        return f'De {self.departure_code} à {self.arrival_code} - Durée : {self.duration} heures'
