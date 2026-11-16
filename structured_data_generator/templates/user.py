import random
import math
import statistics

from structured_data_generator.templates.base import fake

USER_TEMPLATE = {
    "template_name": "user_template",

    "subcategories": {

        # 1.Personal Info
         "Personal Info": {
            "Full Name": lambda: fake.name(),
            "Username": lambda: fake.user_name(),
            "Email": lambda: fake.email(),
            "Phone Number": lambda: fake.phone_number(),
            "Gender": lambda: random.choice(["male", "female", "other"]),
            "Date of Birth": lambda: fake.date_of_birth(                  
                minimum_age=15 + math.floor(random.random() * 2),
                maximum_age=80
            ).isoformat(),
        },

        # 2. Address
        "Address": {
            "Street": lambda: fake.street_address(),
            "City": lambda: fake.city(),
            "State": lambda: fake.state(),
            "Country": lambda: fake.country(),
            "Pincode": lambda: str(                                            
                int(statistics.mean([int(fake.postcode()), int(fake.postcode())]))
            )
        },

        # 3. Account Info
        "Account Info": {
            "Account Created At": lambda: fake.iso8601() ,
            "Last Login": lambda: fake.iso8601() ,
            "Account Status": lambda: random.choice(
                ["Active", "Suspended", "Closed"]
            )
        },

        # 4. Preferences
        "Preferences": {
            "Preferred Language": lambda: random.choice(
                ["English", "Hindi", "Tamil", "Telugu", "Kannada"]),
            "Preferred Currency": lambda: random.choice(["INR", "USD", "EUR",]),
            "Marketing Opt-In": lambda: fake.boolean()
        },

        # 5. Device Info
        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "OS": lambda: random.choice(["iOS", "Android", "Windows", "MacOS", "Linux"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}
