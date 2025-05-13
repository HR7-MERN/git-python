class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.you_saved = price - deal_price
        self.ratings = ratings

    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal_price: {}".format(self.deal_price))
        print("You saved: {}".format(self.you_saved))
        print("Ratings: {}".format(self.ratings))

    def get_deal_price(self):
        return self.deal_price


class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months

    def get_warranty_details(self):
        return self.warranty_in_months

    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} months".format(self.warranty_in_months))


class GroceryItem(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date

    def get_expiry_details(self):
        return self.expiry_date

    def display_product_details(self):
        super().display_product_details()
        print("Expiry_date: {}".format(self.expiry_date))


class Order:
    delivery_charges = {
        "prime_members": 0,
        "non_prime_members": 50
    }

    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_items(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        print("---------------products in cart---------------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("------------------------------------------------")

        print("Delivery_speed: {}".format(self.delivery_speed))
        print("Delivery_address: {}".format(self.delivery_address))
        print("Delivery_charges: {}".format(
            Order.delivery_charges[self.delivery_speed]))

    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print(
            f"Total Bill (including delivery charges): {total_bill + Order.delivery_charges[self.delivery_speed]}.00 Rupees")

        print("Click on submit button to place your order")
        print("Thank you for shopping with us!")


Tv = ElectronicItem("Samsung FHD TV", 50000, 40000, 4.5, 24)
Keyboard = ElectronicItem("Zebronics keyboard", 3000, 2000, 4.5, 24)
Milk = GroceryItem("Amul milk", 35, 30, 4.5, "20/03/2025")
Dairy_milk = GroceryItem("Silk", 35, 30, 4.5, "20/03/2025")
order = Order("non_prime_members", "Bengaluru")
order.add_items(Tv, 1)
order.add_items(Keyboard, 1)
order.add_items(Milk, 3)
order.add_items(Dairy_milk, 5)
order.display_order_details()
order.display_total_bill()
