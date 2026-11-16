import random
import uuid
import math
import statistics
import datetime

from structured_data_generator.templates.base import fake

PRODUCT_CATALOG_TEMPLATE = {
    "Template Name": "product_catalog_template",

    "Subcategories": {

        # 1. Basic Info
        "Basic Info": {
            "Product Id": lambda: str(uuid.uuid4()),
            "Product Name": lambda: fake.catch_phrase(),
            "Category": lambda: random.choice([
                "Electronics", "Fashion", "Home Appliances", "Kitchen", "Books",
                "Furniture", "Beauty", "Groceries", "Automotive", "Sports",
                "Toys", "Pet Supplies", "Healthcare"
            ]),
            "Brand": lambda: fake.company(),
            "Description": lambda: fake.paragraph(nb_sentences=3),
            "Quality Confidence Score": lambda: round(
                math.sqrt(random.uniform(0.1, 1.0)), 3
            )
        },

        # 2. Variants
        "Variants": {
            "Color": lambda: random.choice([
                "Red", "Blue", "Black", "White", "Green", "Yellow", "Grey", None
            ]),
            "Size": lambda: random.choice([
                "S", "M", "L", "XL", "XXL", "32GB", "64GB", "128GB", None
            ]),
            "Material": lambda: random.choice([
                "Plastic", "Steel", "Cotton", "Leather", "Metal", None
            ]),
            "Model Number": lambda: fake.bothify("MDL-###-??"),
            "Variant Score": lambda: round(
                statistics.mean([random.random() for _ in range(3)]), 3
            )
        },

        # 3. Pricing
        "Pricing": {
            "Price": lambda: round(random.uniform(100, 50000), 2),
            "Discount Percent": lambda: random.randint(0, 70),
            "Final Price": lambda: lambda price=None, discount=None: (
                lambda base, disc: round(base - (base * disc / 100), 2)
            )(
                price if price else random.uniform(100, 50000),
                discount if discount else random.randint(0, 70)
            ),
            "Currency": lambda: random.choice(["INR", "USD", "EUR"])
        },

        # 4. Inventory
        "Inventory": {
            "In Stock": lambda: fake.boolean(),
            "Stock Quantity": lambda: random.randint(0, 500),
            "Warehouse Location": lambda: random.choice(
                ["Delhi", "Mumbai", "Chennai", "Bangalore", "Hyderabad"]
            ),
            "Restock Date": lambda: (
                datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 60))
            ).isoformat()
        },

        # 5. Ratings Reviews
        "Ratings Reviews": {
            "Average Rating": lambda: round(random.uniform(1.0, 5.0), 2),
            "Total Reviews": lambda: random.randint(0, 50000),
            "Top Review Title": lambda: fake.sentence(),
            "Top Review Text": lambda: fake.paragraph(nb_sentences=2),
            "Review Weight Score": lambda: round(
                (random.uniform(1, 5) + math.sqrt(random.random())) / 2, 3
            )
        },

        # 6. Timestamps
        "Timestamps": {
            "Released At": lambda: fake.iso8601(),
            "Last Updated At": lambda: (
                datetime.datetime.now() - datetime.timedelta(
                    seconds=random.randint(60, 86400)
                )
            ).isoformat()
        }
    }
}
