from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotion import XItemHalfOff, BuyXGetOneFree, PercentageDiscount, Promotion

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250),
                 NonStockedProduct("Windows License", price=125),
                 LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = XItemHalfOff("Second Half price!",2)
third_one_free = BuyXGetOneFree("Third One Free!", 2)
thirty_percent = PercentageDiscount("30% off!", 0.3)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store("best_buy", product_list)

def show_products(stores):
    """
    Show all products in the store.
    """
    products = stores.get_all_products()
    for product in products:
        print(product.show())
    
    return show_menu_and_get_input(stores)

def show_store_amount(stores):
    """
    Show all products in the store.
    """
    total_quantity = stores.get_total_quantity()
    products = stores.get_all_products()
    print("The total quantity of all products in the store is: ",total_quantity)
    print("\n Detailed list:\n")
    for product in products:
        print(f"{product.name}: {product.get_quantity()}")
    
    return show_menu_and_get_input(stores)

def make_order(stores):
    """
    Make an order by asking the user for product names and quantities.
    """
    shopping_list = []
    product_dict = {}
    products = stores.get_all_products()
    for key, product in enumerate(products, start=1):
        product_dict[key] = product
    while True:
        print("The store has the following products:")
        for key, product in product_dict.items():
            print(key, product.show())
        product_number = input("Enter product number (or 'done' to finish): ")
        if product_number.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        while product_dict[int(product_number)].get_quantity < quantity:
          quantity = int(input(f"There are only {product_dict[int(product_number)].get_quantity} of {product_dict[int(product_number)].name} available. Please enter a valid quantity: "))
        shopping_list.append((product_dict[int(product_number)], quantity))
    
    total_price = stores.order(shopping_list)
    print(f"Total price: ${total_price:.2f}")
    
    return show_menu_and_get_input(stores)

def show_menu_and_get_input(stores):
    """
    Show the menu and get user input.
    If it's a valid option, return a pointer to the function to execute.
    Otherwise, keep asking the user for input.
    """
    selected_stores = stores
    print("Menu:")
    for key, value in FUNCTIONS.items():
        print(f"{key}. {value[1]}")

    # Input loop
    while True:
        try:
            choice = int(input())
            if FUNCTIONS[choice][1] == "Exit":
                print("Goodbye!")
                return FUNCTIONS[choice][0]
            elif choice in FUNCTIONS:
                return FUNCTIONS[choice][0](selected_stores)
        except ValueError as e:
            pass
        print("Try again...")

"""
Function Dispatch Dictionary
"""
FUNCTIONS = { 1: (show_products, "List all products in store"),
              2: (show_store_amount, "Show total amount in store"),
              3: (make_order, "Make an order"),
              4: (quit, "Exit")
             }


def start():

    # The Main Menu loop
    print("The following stores are available:")
    for s in Store.all_instances:
      print(s.name)
    stores_input = input("Enter the store name: ")

    if stores_input in Store.stores.keys():
        print(f"Welcome to {stores_input}!")
    else:
        print(f"Store {stores_input} not found. Exiting...")
        return

    while True:
        choice_func = show_menu_and_get_input(Store.stores[stores_input])
        choice_func()


if __name__ == "__main__":
    start()
