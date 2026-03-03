from Category import Category

class Product: 

    def __init__(self, productId: int, name: str, price: float, category: Category):
        self.productId = productId
        self.name = name
        self.price = price 
        self.category = category

    
