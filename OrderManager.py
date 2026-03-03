from Order import Order

class OrderManager:

    def __init__(self):
        self.orderManager = []

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