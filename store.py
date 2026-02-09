from products import Product


class Store:
    def __init__(self, products=None):
        # type check first
        if products is not None and not isinstance(products, list):
            raise TypeError("products must be a list of Product or None")

        self.products = []

        # check list contents
        if products:
            for p in products:
                if not isinstance(p, Product):
                    raise TypeError("all items in products must be Product instances")
                self.products.append(p)

    def add_product(self, product):
        # type check first
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")

        self.products.append(product)

    def remove_product(self, product):
        # type check first
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")

        # controlled error if missing
        if product not in self.products:
            raise ValueError("product not found in store")

        self.products.remove(product)

    def get_all_products(self):
        return [p for p in self.products if p.is_active()]

    def get_total_quantity(self):
        total = 0
        for p in self.get_all_products():
            total += p.get_quantity()
        return total

    def order(self, shopping_list):
        # nice-to-have: validate early
        if not isinstance(shopping_list, list):
            raise TypeError("shopping_list must be a list of (Product, int) tuples")
        if len(shopping_list) == 0:
            raise ValueError("shopping_list must not be empty")

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("each item must be a tuple (Product, int)")

            product, amount = item

            if not isinstance(product, Product):
                raise TypeError("first element must be a Product")
            if not isinstance(amount, int) or isinstance(amount, bool):
                raise TypeError("second element must be an int")

            if amount <= 0:
                raise ValueError("amount must be > 0")
            if not product.is_active():
                raise ValueError("product is not active")

        total = 0.0
        for product, amount in shopping_list:
            total += product.buy(amount)

        return total
