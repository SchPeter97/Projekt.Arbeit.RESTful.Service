"""
Dummy class to store data while runtime. Pre-filled with some mock data
"""
from typing import Optional

from Product import Product


class Database:
    def __init__(self):
        self.database = []
        self.database.append(Product("Stuhl", "20", "IKEA"))
        self.database.append(Product("Küchentisch", "200", "IKEA"))
        self.database.append(Product("Sofa", "500", "IKEA"))
        self.database.append(Product("Regal", "100", "IKEA"))

    def add(self, product: Product) -> int:
        self.database.append(product)
        print(self.database)
        return len(self.database) - 1

    def remove(self, index: int):
        # don't delete anything, just write to None
        try:
            product = self.database[index]
            product.name = None
            product.price = None
            product.manufacturer = None
            return True
        except IndexError:
            return False

    def create_or_replace(self, product: Product, index: int):
        try:
            self.database[index] = product
            return index
        except IndexError:
            self.database.append(product)
            return len(self.database) - 1

    def modify(self, name: str, price: str, manufacturer: str, index: int):
        try:
            if name is not None:
                self.database[index].name = name
            if price is not None:
                self.database[index].price = price
            if manufacturer is not None:
                self.database[index].manufacturer = manufacturer
            return True
        except IndexError:
            return False

    def get_all(self) -> [Product]:
        data = {}
        for x in range(0, len(self.database)):
            data[x] = self.database[x].serialize()
        return data

    def get(self, index: int) -> Optional[Product]:
        try:
            product = self.database[index]
            if product.name is None or product.price is None or product.manufacturer is None:
                return None
            else:
                return product
        except IndexError:
            return None
