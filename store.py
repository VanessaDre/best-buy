import products


class Store:
    """Store that contains products."""

    def __init__(self, product_list):
        """Create store with a list of products."""
        self.products = product_list


    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)


    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)


    def get_total_quantity(self):
        """Return total quantity of all products."""
        total = 0
        for product in self.products:
            total = total + product.get_quantity()
        return total


    def get_all_products(self):
        """Return a list of active products."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """Buy items from a shopping list and return total price."""
        total_price = 0.0

        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            total_price = total_price + product.buy(quantity)

        return total_price


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()