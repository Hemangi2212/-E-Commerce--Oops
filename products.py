class Product:
    def __init__(self, id, name, price, description, image_url):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url

def get_products():
    return [
        Product(1, "Espresso", 150, "Strong and bold coffee.", "https://upload.wikimedia.org/wikipedia/commons/4/45/A_small_cup_of_coffee.JPG"),
        Product(2, "Cappuccino", 200, "Creamy coffee with milk.", "https://upload.wikimedia.org/wikipedia/commons/c/c8/Cappuccino_at_Sightglass_Coffee.jpg"),
        Product(3, "Latte", 180, "Smooth and milky coffee.", "https://upload.wikimedia.org/wikipedia/commons/7/7c/Cafe_latte_art.jpg")
    ]
