import random

class Util:
    # List of allowed digits 
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Size of the digits list
    size = len(digits)

    @staticmethod
    def generate_city(size):
        # Generates a city as a string with unique digits (no repetition)
        city = ''.join(random.sample(Util.digits, size))
        return city
