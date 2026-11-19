class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

        # Step 2: Calculate total price
        # Step 3: Apply discounts if applicable
        total_price = calculate_total_price(order["items"], order.get("discount_code"))

        # Step 4: Update inventory
        update_inventory(order["items"])

        # Step 5: Generate receipt
        receipt = generate_receipt(order, total_price)

        # Step 6: Send confirmation email
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

        return receipt

def calculate_total_price(items, discount_code=None):
    total_price = sum(item["price"] * item["quantity"] for item in items)
    if discount_code == "SUMMER20":
        total_price *= 0.8  # 20% discount
    elif discount_code == "WELCOME10":
        total_price *= 0.9  # 10% discount
    return total_price

def update_inventory(items):
    for item in items:
        item_id = item["id"]
        quantity = item["quantity"]
        print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

def generate_receipt(order, total_price):
    receipt = f"Customer ID: {order['customer_id']}\n"
    receipt += "Items:\n"
    for item in order["items"]:
        receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
    receipt += f"Total: ${total_price:.2f}\n"
    return receipt