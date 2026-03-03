from Client import Client
from Product import Product

class Order:

    def __init__(self, order_id: int, client: Client):
        self.order_id = order_id
        self.client = client
        self.products = []
        self.total_weight = 0.0

    def add_product(self, product: Product, weight: float):
        self.products.append(product)
        self.total_weight += weight

    def get_total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"Order {self.order_id} - Client: {self.client.name} - Products: {len(self.products)}"
    
