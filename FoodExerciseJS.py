# Creating Class

class Food:
    # Initializer method with 2 parameters
    def __init__(self, name, amount):
        # Updated using name parameter
        self.name = name
        # Updated using amount parameter
        self.amount = amount
        # Updated using private method
        self.price = 0
        # Updated using public method
        self.total = 0
        # Formatted __str__ display function
        self.priceformat = 0
        self.totalformat = 0

# Private method to update price per pound
    def __Price__(self):
        if self.name == "Wagyu Steaks":
            self.price = 450
        elif self.name == "Matsutake Mushrooms":
            self.price = 272
        elif self.name == "Le Bonnotte Potatoes":
            self.price = 270.81
        elif self.name == "Moose Cheese":
            self.price = 487.20
        else:
            self.price = 0

    def get_price(self):
        self.__Price__()
        return self.price

# Public method to update total order price
    def price_total(self):
        self.__Price__()
        self.total = self.price * self.amount
        return self.total

    def price_format(self):
        self.priceformat = "$ {:,.2f}".format(self.price)
        return self.priceformat

    def total_format(self):
        self.totalformat = "$ {:,.2f}".format(self.total)
        return self.totalformat

# str method that returns item overall attributes
    def __str__(self):
        self.price_total()
        self.price_format()
        self.total_format()
        return f"Item: {self.name} \n Amount ordered: {self.amount}\n Price per pound: {self.priceformat}\n Price of order: {self.totalformat}"
