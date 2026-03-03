from Client import Client

class Order:

    def __init__(self, orderId: int, customerName: Client, address: str, weight: float):

        self.orderId = orderId
        self.customerName = customerName
        self.address = address
        self.weight = weight

    
