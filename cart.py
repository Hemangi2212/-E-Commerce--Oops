class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def get_items(self):
        return self.items

    def get_total(self):
        return sum(item.price for item in self.items)

    def clear(self):
        self.items = []
