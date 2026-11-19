class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount_rate)
        print(f"Discounted price for {self.name} ({self.category}): {discounted_price}")
        return discounted_price

    def calculate_tax(self):
        tax = self._round_tax(self.price * self.tax_rate)
        print(f"Tax for {self.name} ({self.category}): {tax}")
        return tax

    def _round_tax(self, tax):
        return tax

class Electronics(Product):
    category = "Electronics"
    discount_rate = 0.10  # 10% discount
    tax_rate = 0.15  # 15% tax

class Clothing(Product):
    category = "Clothing"
    discount_rate = 0.20  # 20% discount
    tax_rate = 0.08  # 8% tax

class Grocery(Product):
    category = "Grocery"
    discount_rate = 0.05  # 5% discount
    tax_rate = 0.02  # 2% tax

    def _round_tax(self, tax):
        return round(tax, 2)  # Grocery tax is rounded to the nearest cent
