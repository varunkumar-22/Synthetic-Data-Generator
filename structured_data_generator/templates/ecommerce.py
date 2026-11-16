import random
import math
import statistics

from structured_data_generator.templates.base import fake

ECOM_TEMPLATE = {
    "template_name": "E-Commerce Transaction Template",

    "subcategories": {

        # 1. Order Info
        "Order Info": {
            "Order ID": lambda: fake.uuid4(),
            "Transaction Date": lambda: fake.iso8601() ,
            "Order Status": lambda: random.choice([
                "Placed", "Paid", "Shipped", "Delivered", "Cancelled", "Returned"
            ]),
            "Total Amount": lambda: round(
                statistics.mean([                   
                    random.uniform(150, 50000),
                    random.uniform(150, 50000)
                ]), 
                2
            ),
            "Currency": lambda: random.choice(["INR", "USD", "EUR"])
        },

        # 2. Customer Details
        "Customer Info": {
            "User ID": lambda: fake.uuid4(),
            "Customer Name": lambda: fake.name(),
            "Customer Email": lambda: fake.email(),
            "Customer Phone": lambda: fake.phone_number()
        },

        # 3. Product Info
        "Product Info": {
            "Product ID": lambda: fake.uuid4(),
            "Product Name": lambda: random.choice([
                "Wireless Earbuds", "Smartphone", "Laptop", "T-Shirt", "Shoes",
                "LED TV", "Bluetooth Speaker", "Backpack", "Keyboard", "Novel Book"
            ]),
            "Category": lambda: random.choice([
                "Electronics", "Fashion", "Home Appliances", "Books", "Grocery",
                "Beauty", "Toys", "Sports", "Automotive", "Furniture"
            ]),
            "Quantity": lambda: max(1, math.floor(random.random() * 6)), 

            "Price Per Unit": lambda: round(random.uniform(100, 20000), 2)     
        },

        # 4. Payment Info
        "Payment Info": {
            "Payment Method": lambda: random.choice([
                "Credit Card", "Debit Card", "UPI", "Wallet", "COD",
                "NetBanking", "EMI", "PayLater", "Gift Card"
            ]),
            "Payment Status": lambda: random.choice(["Success", "Pending", "Failed"]),
            "Transaction ID": lambda: fake.uuid4(),
        },

        # 5. Shipping Info
        "Shipping Info": {
            "Shipping Address": lambda: fake.address().replace("\n", ", "),
            "City": lambda: fake.city(),
            "State": lambda: fake.state(),
            "Country": lambda: fake.country(),
            "Pincode": lambda: str(
                int(statistics.mean([int(fake.postcode()), int(fake.postcode())]))       
            ),

            "Shipping Partner": lambda: random.choice([
                "BlueDart", "Delhivery", "Ecom Express", "FedEx", "DTDC"
            ]),
            "Shipping Status": lambda: random.choice([
                "Not Shipped", "In Transit", "Out for Delivery", "Delivered"
            ])
        },

        # 6. Device Info
        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "OS": lambda: random.choice(["Android", "iOS", "Windows", "MacOS"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}
