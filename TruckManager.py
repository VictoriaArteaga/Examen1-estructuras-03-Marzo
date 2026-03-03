from Inventory import Inventory
from Order import Order

class TruckManager:

    def __init__(self, truck_id: int, max_capacity: float):
        self.truck_id = truck_id
        self.max_capacity = max_capacity
        self.current_weight = 0.0
        self.stack_orders = []

    # Push
    def load_order(self, order: Order):
        if self.current_weight + order.total_weight <= self.max_capacity:
            self.stack_orders.append(order)
            self.current_weight += order.total_weight
            return True
        return False

    # Pop (LIFO)
    def deliver_order(self):
        if not self.is_empty():
            order = self.stack_orders.pop()
            self.current_weight -= order.total_weight
            return order
        return None

    def top_order(self):
        if not self.is_empty():
            return self.stack_orders[-1]
        return None

    def is_empty(self):
        return len(self.stack_orders) == 0

    def size(self):
        return len(self.stack_orders)