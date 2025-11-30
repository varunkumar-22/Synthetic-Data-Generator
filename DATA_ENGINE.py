from faker import Faker
import random
import uuid
import pandas as pd
import math
import stat


fake = Faker(locale="en_US")

# -------------------------------------
# USER TEMPLATE
# -------------------------------------
USER_TEMPLATE = {
    "template_name": "user_template",

    "subcategories": {

        "Personal Info": {
            "full_name": lambda: fake.name(),
            "username": lambda: fake.user_name(),
            "email": lambda: fake.email(),
            "phone_number": lambda: fake.phone_number(),
            "gender": lambda: random.choice(["male", "female", "other"]),
            "date_of_birth": lambda: fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
        },

        "Address": {
            "street": lambda: fake.street_address(),
            "city": lambda: fake.city(),
            "state": lambda: fake.state(),
            "country": lambda: fake.country(),
            "pincode": lambda: fake.postcode()
        },

        "Account_Info": {
            "account_created_at": lambda: fake.iso8601(),
            "last_login": lambda: fake.iso8601(),
            "account_status": lambda: random.choice(["Active", "Suspended", "Closed"])
        },

        "Preferences": {
            "preferred_language": lambda: random.choice(["English", "Hindi", "Tamil", "Telugu", "Kannada"]),
            "preferred_currency": lambda: random.choice(["INR", "USD", "EUR"]),
            "marketing_opt_in": lambda: fake.boolean()
        },

        "Device Info": {
            "device_type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "os": lambda: random.choice(["iOS", "Android", "Windows", "MacOS", "Linux"]),
            "browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}


# --------------------------------------------------------
# GENERATOR WITH COUNT SUPPORT
# --------------------------------------------------------

def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    all_rows = []

    for _ in range(count):
        generated_data = {"id": str(uuid.uuid4())}  # internal only

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    generated_data[field] = fn()

        all_rows.append(generated_data)

    # Convert to DataFrame
    df = pd.DataFrame(all_rows)
    if "id" in df.columns:
        df = df.drop(columns=["id"])


    # Add sequential ID starting from 1
    df.insert(0, "S.no.", range(1, len(df) + 1))

    return df

# --------------------------------------------------------
# TEST RUN
# --------------------------------------------------------

# selected = [ "account_info"]
# df = generate_from_template(USER_TEMPLATE, selected, count=5, seed=42)

# print(df.to_string(index=False))



