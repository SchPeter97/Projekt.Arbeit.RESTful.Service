"""
Product bean
"""


class Product:
    def __init__(self, name: str, price: str, manufacturer: str):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer

    def serialize(self):
        return {
            'name': self.name,
            'price': self.price,
            'manufacturer': self.manufacturer
        }
