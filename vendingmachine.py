class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        # Check if there are enough items in the machine
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")

        # Calculate the total cost of the requested items
        total_cost = req_items * self.item_price

        # Check if the given money is sufficient
        if money < total_cost:
            raise ValueError("Not enough coins")

        # Update the number of items in the machine and calculate the change
        self.num_items -= req_items
        change = money - total_cost

        return change
