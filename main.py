import products
import store


def list_products(best_buy):
    """Print all active products with numbers."""
    all_products = best_buy.get_all_products()

    print("------")
    for i, product in enumerate(all_products, start=1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("------")


def show_total(best_buy):
    """Print total quantity in store."""
    total = best_buy.get_total_quantity()
    print(f"Total of {total} items in store")


def make_order(best_buy):
    """Let the user build a shopping list and place an order."""
    all_products = best_buy.get_all_products()
    shopping_list = []

    print("------")
    for i, product in enumerate(all_products, start=1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("------")

    print("When you want to finish order, enter empty text.")

    while True:
        product_number = input("Which product # do you want? ").strip()
        if product_number == "":
            break

        if not product_number.isdigit():
            print("Please enter a valid number.")
            continue

        product_index = int(product_number) - 1
        if product_index < 0 or product_index >= len(all_products):
            print("Product number does not exist.")
            continue

        amount_text = input("What amount do you want? ").strip()
        if not amount_text.isdigit():
            print("Please enter a valid amount.")
            continue

        amount = int(amount_text)
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        shopping_list.append((all_products[product_index], amount))
        print("Product added to list!")

    if len(shopping_list) == 0:
        print("No products ordered.")
        return

    try:
        total_price = best_buy.order(shopping_list)
        print(f"******** Order made! Total payment: ${total_price}")
    except Exception as e:
        print(f"Order failed: {e}")


def start(best_buy):
    """Start the store menu loop."""
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            show_total(best_buy)
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
