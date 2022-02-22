class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        pass

    def print_info(self):
        print(self.name, self.category, self.price)