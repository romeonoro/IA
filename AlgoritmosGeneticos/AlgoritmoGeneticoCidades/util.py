import random

class Util:
    # List of allowed digits
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    size = len(digits)

    @staticmethod
    def generate_city(size):
        # Generates a city as a list of unique digits (no repetition)
        return random.sample(Util.digits, size)
