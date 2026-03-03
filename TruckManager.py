from Inventory import Inventory
from Order import Order

class TruckManager:

    def __init__(self, truckId: int, inventory: Inventory, order: Order):

        self.truckId = truckId
        self.inventory = inventory
        self.order = order
        self.managerTruck = []


    def isEmpty(self):
        return len(self.managerTruck) == 0

    def loadOrder(self, order: Order):
        self.managerTruck.append(order)

    def deliverOrder(self):
        if not self.isEmpty():
            return self.managerTruck.pop(0)
        else:
            return None
        
    def topOrder(self):
        if not self.isEmpty():
            return self.managerTruck[0]
        else:
            return None
        
    def sizeOrders(self):
        return len(self.managerTruck)