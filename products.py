class Product:
    """A product in the store."""
    def __init__(self, name, price, quantity):
        """Create a product with name, price and quantity."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if name.strip() == "":
            raise ValueError("Name can't be empty.")

        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if price < 0:
            raise ValueError("Price can't be negative.")

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an int.")
        if quantity < 0:
            raise ValueError("Quantity can't be negative.")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity
        self.active = self.quantity > 0


    def get_quantity(self):
        """Return current quantity."""
        return self.quantity


    def set_quantity(self, quantity):
        """Set quantity and update active status."""
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an int.")
        if quantity < 0:
            raise ValueError("Quantity can't be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.active = False
        else:
            self.active = True


    def is_active(self):
        """Return True if product is active."""
        return self.active


    def activate(self):
        """Activate the product."""
        self.active = True


    def deactivate(self):
        """Deactivate the product."""
        self.active = False


    def show(self):
        """Print product info."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """Buy quantity and return total price."""
        if not self.active:
            raise ValueError("Product is not active.")

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an int.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if quantity > self.quantity:
            raise ValueError("Not enough stock.")

        total_price = self.price * quantity
        self.quantity = self.quantity - quantity

        if self.quantity == 0:
            self.active = False

        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()