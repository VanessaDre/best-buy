from products import Product
from store import Store


def format_money(value):
    if float(value).is_integer():
        return f"${int(value)}"
    return f"${value:.2f}"


def print_products(store):
    products = store.get_all_products()
    print("------")
    index = 1
    for product in products:
        print(f"{index}. {product.show()}")
        index += 1
    print("------")
    return products


def show_menu():
    print()
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def make_order(store):
    products = print_products(store)
    if not products:
        print("No active products in store.")
        return

    print("When you want to finish order, enter empty text.")
    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ").strip()
        if product_input == "":
            break
        if not product_input.isdigit():
            print("Invalid product number.")
            continue

        product_num = int(product_input)
        if product_num <= 0 or product_num > len(products):
            print("Invalid product number.")
            continue

        amount_input = input("What amount do you want? ").strip()
        if amount_input == "" or not amount_input.isdigit():
            print("Invalid amount.")
            continue

        amount = int(amount_input)
        if amount <= 0:
            print("Amount must be a positive integer.")
            continue

        product = products[product_num - 1]
        if amount > product.get_quantity():
            print("Not enough stock.")
            continue

        shopping_list.append((product, amount))
        print("Product added to list!")

    if not shopping_list:
        print("********")
        print("No items ordered.")
        return

    total_payment = store.order(shopping_list)
    print("********")
    print(f"Order made! Total payment: {format_money(total_payment)}")


def main():
    store = Store(
        [
            Product("MacBook Air M2", 1450, 100),
            Product("Bose QuietComfort Earbuds", 250, 500),
            Product("Google Pixel 7", 500, 250),
        ]
    )

    while True:
        show_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            print_products(store)
        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

