from Inventory import Inventory
from Product import Product

class Truck: 

    def __init__(self, truckId: int, inventory: Inventory, product: Product):

        self.truckId = truckId
        self.inventory = inventory
        self.product = product
        self.orderManager = []


    def isEmpty(self):
        return len(self.orderManager) == 0

    def addOrder(self, order):
        self.orderManager.append(order)

    def deliverOrder(self):
        if not self.isEmpty():
            return self.orderManager.pop(0)
        else:
            return None
        
    def topOrder(self):
        if not self.isEmpty():
            return self.orderManager[0]
        else:
            return None
        
    def sizeOrders(self):
        return len(self.orderManager)

    
        
