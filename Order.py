from Client import Client

class Order:

    def __init__(self, orderId: int, customerName: Client, address: str, weight: float):

        self.orderId = orderId
        self.customerName = customerName
        self.address = address
        self.weight = weight
        self.queueOrders = []

    def addOrder(self, order):
        self.queueOrders.append(order)

    def removeOrder(self):
        if not self.isEmpty():
            return self.queueOrders.pop(0)
        else:
            return None
        

    def isEmpty(self):
        return len(self.queueOrders) == 0
    
    def size(self):
        return len(self.queueOrders)
    
    def frontOrder(self):
        if not self.isEmpty():
            return self.queueOrders[0]
        else:
            return None

    def rearOrder(self):
        if not self.isEmpty():
            return self.queueOrders[-1]
        else:
            return None
