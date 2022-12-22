class Airport:
    def __init__(self, name: str = None, code: str = None, lat: float = None, longitude: float = None):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = longitude

    def __str__(self):
        return f'{self.name} ({self.code}) - Latitude : {self.lat} / Longitude : {self.long}'
