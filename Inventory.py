from Product import Product

class Inventory: 

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.storage = [[None for _ in range(cols)] for _ in range(rows)]

    def add_product(self, product: Product, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.storage[row][col] = product
            return True
        return False

    def remove_product(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            product = self.storage[row][col]
            self.storage[row][col] = None
            return product
        return None

    def get_product(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.storage[row][col]
        return None

    def show_inventory(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.storage[i][j]:
                    print(f"[{self.storage[i][j].name}]", end=" ")
                else:
                    print("[Empty]", end=" ")
            print()

    