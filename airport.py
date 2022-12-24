class Airport:
    def __init__(self, name: str = None, code: str = None, lat: float = None, longitude: float = None):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = longitude

    def __str__(self):
        return f'{self.name} ({self.code}) - Latitude : {self.lat} / Longitude : {self.long}'


def test_airport():
    # Création d'un objet Airport avec des valeurs par défaut
    airport1 = Airport()
    # Vérification que l'objet Airport est bien initialisé avec des valeurs par défaut
    assert airport1.name == None
    assert airport1.code == None
    assert airport1.lat == None
    assert airport1.long == None
    # Vérification que la méthode __str__ renvoie une chaîne de caractères correcte
    assert str(airport1) == 'None (None) - Latitude : None / Longitude : None'

    # Création d'un objet Airport avec des valeurs spécifiques
    airport2 = Airport('Paris Charles de Gaulle', 'CDG', 49.012779, 2.55)
    # Vérification que l'objet Airport est bien initialisé avec les bonnes valeurs
    assert airport2.name == 'Paris Charles de Gaulle'
    assert airport2.code == 'CDG'
    assert airport2.lat == 49.012779
    assert airport2.long == 2.55
    # Vérification que la méthode __str__ renvoie une chaîne de caractères correcte
    assert str(
        airport2) == 'Paris Charles de Gaulle (CDG) - Latitude : 49.012779 / Longitude : 2.55'


# Appel de la fonction de test
test_airport()

