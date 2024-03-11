class Order:
    def __init__(self, products, quantities, prices):
        self.__products = products
        self.__quantities = quantities
        self.__prices = prices

    def total_cost(self):
        return sum([quantity * price for quantity, price in zip(self.__quantities, self.__prices)])

class Customer:
    def __init__(self, name):
        self.name = name

    def place_order(self, products, quantities, prices, order_processor):
        order = Order(products, quantities, prices)
        order_processor.process_order(order, self)

class OrderProcessor:
    def process_order(self, order, customer):
        total_cost = order.total_cost()
        print(f"Processing order for customer {customer.name}:")
        for product, quantity in zip(order._Order__products, order._Order__quantities):
            print(f"- {quantity} {product}")
        print(f"Total cost: ${total_cost}")

# Example usage
customer = Customer("John Doe")
order_processor = OrderProcessor()
customer.place_order(["Phone", "Laptop", "Tablet"], [1, 2, 1], [800, 1200, 400], order_processor)
