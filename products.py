class Product:
    def __init__(self, name, price, quantity):
        # type checks first
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("price must be a number")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("quantity must be an int")

        # value checks second
        if name.strip() == "":
            raise ValueError("name can't be empty")
        if price <= 0:
            raise ValueError("price must be > 0")
        if quantity < 0:
            raise ValueError("quantity can't be negative")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity
        self.active = self.quantity > 0

    def is_active(self):
        return self.active

    def activate(self):
        if self.quantity <= 0:
            raise ValueError("cannot activate product with zero quantity")
        self.active = True

    def deactivate(self):
        self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        # type check first
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("quantity must be an int")

        # value check second
        if quantity < 0:
            raise ValueError("quantity can't be negative")

        self.quantity = quantity
        self.active = self.quantity > 0

    def buy(self, quantity):
        # type check first
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("quantity must be an int")

        # value check second
        if quantity <= 0:
            raise ValueError("quantity must be > 0")
        if not self.is_active():
            raise ValueError("product is not active")
        if quantity > self.quantity:
            raise ValueError("not enough stock")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
