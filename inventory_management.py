# Class to add and manage customers
class CustomerMaster:
    customers = []

    def __init__(self):
        pass

    def info(self):
        while True:
            cnt = input("Press any key to exit or 'y' to add data: ").lower()

            if cnt == 'y':
                name = input("Enter your name: ")
                cust_type = input("Enter type (customer / vendor): ")
                pan = input("Enter PAN number: ")

                # Ensure PAN is unique
                if any(cust['pan'] == pan for cust in CustomerMaster.customers):
                    print("PAN number already exists. Please enter a unique PAN.")
                    continue

                CustomerMaster.customers.append({
                    'id': len(CustomerMaster.customers)+1,
                    'name': name,
                    'type': cust_type,
                    'pan': pan
                })
            else:
                break

    def display(self):
        print("\n--- Customer Records ---")
        for cust in CustomerMaster.customers:
            print(f"Name : {cust['name']}")
            print(f"Type : {cust['type']}")
            print(f"PAN  : {cust['pan']}\n")


# Class to add and manage product details
class ProductManager:
    product = []  # Class-level list to allow stockMaster access

    def __init__(self):
        pass

    def info(self):
        while True:
            cnt = input(
                "Press y to continue and any key to exit and print : ").lower()

            if cnt == 'y':
                name = input("Enter product name : ")
                inc = 0
                out = 0
                onhand = inc - out

                ProductManager.product.append({
                    'id': len(ProductManager.product)+1,
                    'name': name,
                    'inc': inc,
                    'out': out,
                    'onhand': onhand
                })
            else:
                break

    def display(self):
        print("\n--- Product details ---")
        for pro in ProductManager.product:
            print(f"\nName : {pro['name']}")
            print(f"Incoming : {pro['inc']}")
            print(f"Outgoing  : {pro['out']}")
            print(f"Onhand : {pro['onhand']}")

            if pro['onhand'] < 0:
                print(" There should be validate to not sale more than onhand")


# Class to handle stock transactions
class stockMaster:
    def __init__(self):
        self.stock = []

    def info(self):
        while True:
            cnt = input(
                "Press y to continue and any key to exit and print : ").lower()

            if cnt == 'y':
                # Ensure at least one product and customer exist
                if not ProductManager.product or not CustomerMaster.customers:
                    print("Please add product and customer details first.")
                    break

                try:
                    pro_id = int(input("Enter product id : "))
                    product = next(
                        (p for p in ProductManager.product if p['id'] == pro_id), None)
                    if not product:
                        print("Invalid product ID.")
                        continue

                    cust_id = int(input("Enter customer id : "))
                    customer = next(
                        (c for c in CustomerMaster.customers if c['id'] == cust_id), None)
                    if not customer:
                        print("Invalid customer ID.")
                        continue

                    qty = int(input("Enter quantity : "))
                    type = input("Enter type (Outgoing/incoming) :").lower()

                    if type == 'incoming':
                        product['inc'] += qty
                    elif type == 'outgoing':
                        if qty > product['onhand']:
                            print(
                                " There should be validate to not sale more than onhand")
                            continue
                        product['out'] += qty
                    else:
                        print("Invalid type.")
                        continue

                    product['onhand'] = product['inc'] - product['out']

                    self.stock.append({
                        'id': len(self.stock)+1,
                        'product_id': pro_id,
                        'customer_id': cust_id,
                        'quantity': qty,
                        'type': type
                    })
                except:
                    print("Invalid input.")
                    continue
            else:
                break

    def display(self):
        print("\n--- Stock Records ---")
        for stock in self.stock:
            print(f"Product ID : {stock['product_id']}")
            print(f"Customer ID : {stock['customer_id']}")
            print(f"Quantity : {stock['quantity']}")
            print(f"Type : {stock['type']}\n")


# Main controller class to handle customer, product, and stock (placed last as requested)
class customize:
    def __init__(self):
        # Initialize customer, product, and stock classes
        self.customer = CustomerMaster()
        self.product = ProductManager()
        self.stock = stockMaster()

    def info(self):
        while True:
            print("\n1. Customer Details")
            print("2. Product Details")
            print("3. Stock Details")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.customer.info()
                self.customer.display()
            elif choice == '2':
                self.product.info()
                self.product.display()
            elif choice == '3':
                self.stock.info()
                self.stock.display()
            elif choice == '4':
                print("\n--- Final Customer, Product, and Stock Details ---")
                self.customer.display()
                self.product.display()
                self.stock.display()
                break
            else:
                print("Invalid choice, please try again.")


# Run the program only if executed directly
if __name__ == "__main__":
    c = customize()
    c.info()
