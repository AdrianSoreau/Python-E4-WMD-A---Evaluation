class Flight:
    def __init__(self, src_code: str = None, dst_code: str = None, duration: float = None):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

    def __str__(self):
        return f'De {self.src_code} à {self.dst_code} - Durée : {self.duration} heures'


def test_flight():
    # Création d'un objet Flight avec des valeurs de test
    flight = Flight(src_code='CDG', dst_code='AMS', duration=1.5)

    # Vérification de la valeur de la propriété src_code
    assert flight.src_code == 'CDG', f'Mauvaise valeur pour src_code : {flight.src_code}'

    # Vérification de la valeur de la propriété dst_code
    assert flight.dst_code == 'AMS', f'Mauvaise valeur pour dst_code : {flight.dst_code}'

    # Vérification de la valeur de la propriété duration
    assert flight.duration == 1.5, f'Mauvaise valeur pour duration : {flight.duration}'

    # Vérification de la chaîne de caractères renvoyée par __str__
    assert str(
        flight) == 'De CDG à AMS - Durée : 1.5 heures', f'Mauvaise chaîne de caractères renvoyée par __str__ : {str(flight)}'


# Appel de la fonction de test
test_flight()
