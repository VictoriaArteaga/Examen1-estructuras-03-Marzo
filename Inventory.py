from Product import Product

class Inventory: 

    def __init__(self, product: Product, numAisle: int, numShelf: int):

        self.product = product
        self.numAisle = numAisle
        self.numShelf = numShelf
        self.inventoryManager = []

    