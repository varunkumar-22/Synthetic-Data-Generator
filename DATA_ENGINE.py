from faker import Faker
import random
import uuid
import pandas as pd
import math
import statistics
import time
import datetime

fake = Faker(locale="en_US")
# && -- Used Math
# @@ -- Used time
# ** -- Used statistics

# ----------USER TEMPLATE----------

USER_TEMPLATE = {
    "template_name": "user_template",

    "subcategories": {
         "Personal Info": {
            "Full Name": lambda: fake.name(),
            "Username": lambda: fake.user_name(),
            "Email": lambda: fake.email(),
            "Phone Number": lambda: fake.phone_number(),
            "Gender": lambda: random.choice(["male", "female", "other"]),
            "Date of Birth": lambda: fake.date_of_birth(                  #&&&
                minimum_age=15 + math.floor(random.random() * 2),
                maximum_age=80
            ).isoformat(),
        },

        "Address": {
            "Street": lambda: fake.street_address(),
            "City": lambda: fake.city(),
            "State": lambda: fake.state(),
            "Country": lambda: fake.country(),
            "Pincode": lambda: str(                                            #***
                int(statistics.mean([int(fake.postcode()), int(fake.postcode())]))
            )
        },

        "Account Info": {
            "Account Created At": lambda: fake.iso8601() + f" (ts:{int(time.time())})", #@@
            "Last Login": lambda: fake.iso8601() + f" (ts:{int(time.time())})", #@@

            "Account Status": lambda: random.choice(
                ["Active", "Suspended", "Closed"]
            )
        },

        "Preferences": {
            "Preferred Language": lambda: random.choice(
                ["English", "Hindi", "Tamil", "Telugu", "Kannada"]),
            "Preferred Currency": lambda: random.choice(["INR", "USD", "EUR",]),
            "Marketing Opt-In": lambda: fake.boolean()
        },

        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "OS": lambda: random.choice(["iOS", "Android", "Windows", "MacOS", "Linux"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}




# ----------GENERATOR FUNCTION----------

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



# ----------ECOM TEMPLATE ----------

ECOM_TEMPLATE = {
    "template_name": "E-Commerce Transaction Template",

    "subcategories": {

        # 1. Order Info
        "Order Info": {
            "Order ID": lambda: fake.uuid4(),

            # Add UNIX time noise using time + math
            "Transaction Date": lambda: fake.iso8601() + f" (ts:{int(time.time() + math.floor(random.random() * 100))})", #@@@

            "Order Status": lambda: random.choice([
                "Placed", "Paid", "Shipped", "Delivered", "Cancelled", "Returned"
            ]),

            # Add simple price smoothening using statistics
            "Total Amount": lambda: round(
                statistics.mean([                    #****
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
            "Quantity": lambda: max(1, math.floor(random.random() * 6)),  #&&&&

            "Price Per Unit": lambda: round(random.uniform(100, 20000), 2)      #&&&
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
                int(statistics.mean([int(fake.postcode()), int(fake.postcode())]))         #*****
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



FINANCIAL_TEMPLATE = {
    "template_name": "financial_banking_transaction_template",

    "subcategories": {

        # 1. Account Information
        "Account Info": {
            "Account ID": lambda: fake.uuid4(),
            "Account Type": lambda: random.choice(["Savings", "Current", "Salary", "NRE", "NRO", "Fixed Deposit"]),
            "Bank Name": lambda: random.choice([
                "HDFC Bank", "ICICI Bank", "SBI", "Axis Bank", "Kotak Mahindra Bank",
                "Yes Bank", "Punjab National Bank", "Bank of Baroda"
            ]),
            "Branch": lambda: fake.city(),
            "IFSC Code": lambda: "BANK" + str(int(math.fabs(random.randint(10000, 99999)))),
            "Account Holder Name": lambda: fake.name()
        },

        # 2. Transaction Details
        "Transaction Info": {
            "Transaction ID": lambda: fake.uuid4(),
            "Transaction Date": lambda: fake.iso8601(),

            "Transaction Type": lambda: random.choice([
                "Deposit", "Withdrawal", "Online Transfer", "UPI Payment", "Card Payment",
                "Loan EMI", "Interest Credit", "Service Charge"
            ]),

            # Using math to round amount cleanly
            "Amount": lambda: math.floor(random.uniform(100, 200000) * 100) / 100,

            "Currency": lambda: random.choice(["INR", "USD", "EUR"]),
            "Transaction Status": lambda: random.choice(["Success", "Pending", "Failed"])
        },

        # 3. Customer Information
        "Customer Info": {
            "Customer ID": lambda: fake.uuid4(),
            "Customer Name": lambda: fake.name(),
            "Email": lambda: fake.email(),
            "Phone Number": lambda: fake.phone_number(),

            # Using statistics to generate a mix of digits (looks realistic)
            "PAN Number": lambda: "".join([chr(random.randint(65, 90)) for _ in range(5)]) +
                                  str(statistics.mean([random.randint(1000, 9999), random.randint(1000, 9999)])).split(".")[0] +
                                  chr(random.randint(65, 90)),

            "Aadhaar Last4": lambda: random.randint(1000, 9999)
        },

        # 4. Card Details (Optional)
        "Card Info": {
            "Card Type": lambda: random.choice(["Debit Card", "Credit Card", "Prepaid Card"]),
            "Card Network": lambda: random.choice(["Visa", "Mastercard", "RuPay", "American Express"]),
            "Card Last4": lambda: random.randint(1000, 9999),

            # Using time-based randomness
            "Card Issuer Bank": lambda: random.choice([
                "SBI", "HDFC", "ICICI", "Axis Bank", "Kotak", "Punjab National Bank"
            ])
        },

        # 5. Loan Details (Optional)
        "Loan Info": {
            "Loan ID": lambda: fake.uuid4(),
            "Loan Type": lambda: random.choice(["Home Loan", "Personal Loan", "Car Loan", "Education Loan"]),
            "Loan Amount": lambda: round(random.uniform(50000, 2500000), 2),
            "Interest Rate": lambda: round(random.uniform(6.5, 14.0), 2),

            # Using math to compute a realistic EMI variation
            "EMI Amount": lambda: math.ceil(random.uniform(2000, 50000))
        },

        # 6. Device Information
        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "OS": lambda: random.choice(["Android", "iOS", "Windows", "MacOS", "Linux"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}


IOT_SENSOR_TEMPLATE = {
    "template_name": "iot_sensor_template",

    "subcategories": {

        # Device Information
        "Device Info": {
            "Device ID": lambda: f"DEV-{fake.random_int(1000, 9999)}",

            # Making device type more readable (title case)
            "Device Type": lambda: random.choice([
                "Temperature Sensor", "Humidity Sensor", "Motion Detector",
                "Air Quality Monitor", "GPS Tracker", "Power Meter"
            ]),

            # Using math for version formatting
            "Firmware Version": lambda: f"{math.floor(random.uniform(1, 4))}."
                                       f"{math.floor(random.uniform(0, 10))}."
                                       f"{math.floor(random.uniform(0, 10))}",

            "Manufacturer": lambda: random.choice(["Bosch", "Siemens", "Honeywell", "Xiaomi", "Philips"])
        },

        # Location Data
        "Location Data": {
            "Latitude": lambda: fake.latitude(),
            "Longitude": lambda: fake.longitude(),

            # Using stats to smooth random values
            "Altitude Meters": lambda: round(
                statistics.mean([random.uniform(5, 2000), random.uniform(5, 2000)]), 2
            ),

            "Zone": lambda: random.choice(["Zone A", "Zone B", "Zone C"])
        },

        # Sensor Readings
        "Sensor Readings": {
            # Using mean for natural temperature variation
            "Temperature C": lambda: round(statistics.mean([
                random.uniform(15.0, 45.0),
                random.uniform(15.0, 45.0)
            ]), 2),

            # Using math.ceil for humidity rounding
            "Humidity Percent": lambda: math.ceil(random.uniform(20.0, 90.0)),

            "Air Quality Index": lambda: fake.random_int(10, 300),
            "CO2 PPM": lambda: fake.random_int(350, 2000),
            "Motion Detected": lambda: fake.boolean()
        },

        # Network Data
        "Network Data": {
            "Signal Strength dBm": lambda: fake.random_int(-100, -40),
            "Connection Type": lambda: random.choice(["WiFi", "LTE", "LoRaWAN", "ZigBee"]),
            "IP Address": lambda: fake.ipv4()
        },

        # Battery / Power Info
        "Battery Power": {
            "Battery Level Percent": lambda: fake.random_int(10, 100),
            "Battery Health": lambda: random.choice(["Good", "Moderate", "Weak"]),

            # Using math to randomly toggle states
            "Charging Status": lambda: "Charging" if math.floor(random.random() * 2) == 1 else "Not Charging"
        },

        # Timestamp Information
        "Timestamp Info": {
            # Using time library for current timestamp
            "Timestamp": lambda: time.strftime("%Y-%m-%dT%H:%M:%S"),

            # Keeping maintenance realistic (from this year)
            "Last Maintenance": lambda: fake.date_this_year().isoformat()
        }
    }
}



NLP_TEXT_TEMPLATE = {
    "template_name": "nlp_text_template",

    "subcategories": {

        "Basic Text": {
            "Sentence": lambda: fake.sentence(),
            "Short Paragraph": lambda: fake.paragraph(nb_sentences=3),
            "Long Paragraph": lambda: fake.paragraph(nb_sentences=7),
            "Word": lambda: fake.word(),
            "Keywords": lambda: ", ".join(fake.words(nb=5))
        },

        "Document Metadata": {
            "Title": lambda: fake.sentence(nb_words=4),
            "Author": lambda: fake.name(),
            "Published Year": lambda: fake.year(),
            # using math.floor just to show a math function
            "Document Type": lambda: ["Article", "Blog", "Research Paper", "Report", "Review", "Story"]
                                    [math.floor(random.uniform(0, 5.99))]
        },

        "NLP Annotations": {
            # using statistics.mean with simple values
            "Language": lambda: random.choice(["en", "hi", "ta", "fr", "es"]),
            "Sentiment": lambda: random.choice(["Positive", "Negative", "Neutral"]),
            "Emotion": lambda: random.choice(["Joy", "Anger", "Sadness", "Fear", "Neutral"]),
            "Toxicity Flag": lambda: fake.boolean(),
            "Reading Level": lambda: random.choice(["Easy", "Moderate", "Complex"])
        },

        "Synthetic NER Data": {
            "Person Name": lambda: fake.name(),
            "Location Name": lambda: fake.city(),
            "Organization": lambda: fake.company(),
            "Misc Entity": lambda: random.choice(["COVID-19", "AI", "Climate", "Blockchain", "Quantum"])
        },

        "Text Stats": {
            # using math.ceil + math.sqrt for small transformations
            "Word Count": lambda: math.ceil(math.sqrt(fake.random_int(20, 900))),
            "Char Count": lambda: fake.random_int(50, 1200),

            # using statistics.mean to calculate avg word length from random numbers
            "Average Word Length": lambda: round(
                statistics.mean([random.uniform(3.0, 8.0) for _ in range(5)]), 2
            ),

            "Unique Words": lambda: fake.random_int(5, 80)
        },

        "Timestamp Info": {
            # Using time.time() → UNIX timestamp, then converting with math.floor
            "Created At": lambda: f"UNIX-{math.floor(time.time())}",
            "Updated At": lambda: fake.iso8601()
        }
    }
}


WEB_ANALYTICS_TEMPLATE = {
    "Template Name": "web_analytics_template",

    "Subcategories": {

        # ==============================
        # USER SESSION INFO
        # ==============================
        "Session Info": {
            "Session Id": lambda: str(uuid.uuid4()),
            "User Id": lambda: fake.uuid4(),

            "Session Start": lambda: datetime.datetime.now().isoformat(),
            "Session End": lambda: (
                datetime.datetime.now() + datetime.timedelta(
                    seconds=random.randint(5, 3600)
                )
            ).isoformat(),

            "Session Duration Sec": lambda: random.randint(5, 3600),
            "Is New User": lambda: fake.boolean(),

            "Engagement Score": lambda: round(
                random.betavariate(2, 4), 3
            ),
        },

        # ==============================
        # PAGE VIEW METRICS
        # ==============================
        "Page Metrics": {
            "Page Url": lambda: fake.uri(),
            "Referrer Url": lambda: random.choice([fake.uri(), None]),
            "Page Title": lambda: fake.sentence(nb_words=4),

            "Time On Page Sec": lambda: random.randint(1, 900),
            "Scroll Depth Percent": lambda: random.randint(10, 100),
            "Interaction": lambda: random.choice(["click", "scroll", "hover", "input", "none"]),

            "Ctr": lambda: round(random.uniform(0.01, 0.4), 3),

            "Bounce Probability": lambda: round(random.betavariate(3, 5), 3)
        },

        # ==============================
        # TRAFFIC SOURCE
        # ==============================
        "Traffic Source": {
            "Source": lambda: random.choice(["Direct", "Organic", "Paid", "Referral", "Social"]),
            "Medium": lambda: random.choice(["none", "cpc", "email", "banner", "social"]),
            "Campaign": lambda: random.choice(["summer_sale", "new_launch", "retargeting", "none"]),
            "Keyword": lambda: random.choice([fake.word(), None]),

            "Traffic Quality": lambda: round(
                statistics.mean([random.random() for _ in range(3)]), 3
            )
        },

        # ==============================
        # DEVICE & BROWSER INFO
        # ==============================
        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"]),
            "Os": lambda: random.choice(["Windows", "MacOS", "Android", "iOS", "Linux"]),
            "Screen Resolution": lambda: random.choice([
                "1920x1080", "1366x768", "1536x864", "1280x720", "1440x900"
            ]),

            "Device Performance Score": lambda: round(
                math.sqrt(random.uniform(1, 100)), 2
            )
        },

        # ==============================
        # LOCATION / GEO DATA
        # ==============================
        "Geo Data": {
            "Ip Address": lambda: fake.ipv4_public(),
            "Country": lambda: fake.country(),
            "City": lambda: fake.city(),
            "Timezone": lambda: fake.timezone(),

            "Avg Network Latency Ms": lambda: random.randint(20, 300)
        },

        # ==============================
        # PERFORMANCE DATA
        # ==============================
        "Performance": {
            "Page Load Time Ms": lambda: random.randint(200, 5000),
            "Dns Lookup Ms": lambda: random.randint(10, 300),
            "Ttfb Ms": lambda: random.randint(50, 1200),
            "Total Resources Loaded": lambda: random.randint(5, 100),
            "Js Errors": lambda: random.randint(0, 10),

            "Performance Score": lambda: round(random.uniform(40, 100), 2),

            "Avg Resource Size Kb": lambda: round(
                statistics.mean([random.randint(20, 500) for _ in range(5)]), 2
            )
        }
    }
}




IMAGE_METADATA_TEMPLATE = {
    "Template Name": "image_metadata_template",

    "Subcategories": {

        # ==============================
        # BASIC IMAGE INFO
        # ==============================
        "Basic Info": {
            "Image Id": lambda: str(uuid.uuid4()),
            "File Name": lambda: fake.file_name(category="image"),
            "File Format": lambda: random.choice(["jpg", "jpeg", "png", "webp", "tiff"]),
            "File Size Kb": lambda: random.randint(50, 15000),  # 50 KB – 15 MB
            "Color Mode": lambda: random.choice(["RGB", "RGBA", "CMYK", "Grayscale"]),
            "Entropy Score": lambda: round(random.uniform(2.0, 7.5), 3)
        },

        # ==============================
        # DIMENSIONS & QUALITY
        # ==============================
        "Dimensions": {
            "Width Px": lambda: random.randint(256, 8000),
            "Height Px": lambda: random.randint(256, 8000),
            "Aspect Ratio": lambda: f"{random.choice([1,4,16,3])}:{random.choice([1,3,9,2])}",
            "Dpi": lambda: random.choice([72, 96, 150, 300]),
            "Clarity Score": lambda: round(math.sqrt(random.uniform(1, 100)), 2)
        },

        # ==============================
        # CAMERA / EXIF DATA
        # ==============================
        "Camera Exif": {
            "Camera Make": lambda: random.choice(["Canon", "Nikon", "Sony", "Fujifilm", "Apple", "Samsung"]),
            "Camera Model": lambda: fake.word(),
            "Lens Model": lambda: random.choice(["18-55mm", "24-70mm", "50mm", "70-200mm", None]),
            "Focal Length Mm": lambda: random.randint(10, 200),
            "Aperture": lambda: random.choice(["f/1.8", "f/2.0", "f/2.8", "f/4", "f/5.6"]),
            "Iso": lambda: random.choice([100, 200, 400, 800, 1600, 3200]),
            "Exposure Time": lambda: random.choice(["1/50", "1/100", "1/200", "1/500"]),
            "Noise Level": lambda: round(random.betavariate(2, 6), 3)
        },

        # ==============================
        # GEOLOCATION INFO
        # ==============================
        "Geolocation": {
            "Latitude": lambda: float(fake.latitude()),
            "Longitude": lambda: float(fake.longitude()),
            "Country": lambda: fake.country(),
            "City": lambda: fake.city(),
            "Gps Accuracy Meters": lambda: random.randint(3, 100)
        },

        # ==============================
        # CONTENT TAGS / LABELS
        # ==============================
        "Tags Labels": {
            "Primary Label": lambda: random.choice([
                "person", "animal", "landscape", "food", "vehicle", "object", "logo",
                "indoor", "outdoor", "nature", "architectural"
            ]),
            "Secondary Labels": lambda: ", ".join(fake.words(nb=3)),
            "Confidence Score": lambda: round(random.uniform(0.5, 1.0), 3),
            "Aesthetic Score": lambda: round(random.uniform(0.2, 0.99), 3)
        },

        # ==============================
        # COLOR PROFILE STATS
        # ==============================
        "Color Stats": {
            "Dominant Color": lambda: random.choice(["red", "blue", "green", "yellow", "white", "black", "orange"]),
            "Color Variance": lambda: round(
                statistics.mean([random.uniform(0.1, 1) for _ in range(5)]), 3
            ),
            "Brightness Level": lambda: round(random.uniform(0.1, 0.9), 3),
            "Contrast Ratio": lambda: round(random.uniform(1.0, 5.0), 2)
        },

        # ==============================
        # TIMESTAMP INFO
        # ==============================
        "Timestamp Info": {
            "Created At": lambda: datetime.datetime.now().isoformat(),
            "Uploaded At": lambda: datetime.datetime.now().isoformat(),
            "Last Modified At": lambda: (
                datetime.datetime.now() - datetime.timedelta(
                    minutes=random.randint(1, 2000)
                )
            ).isoformat()
        }
    }
}


EDU_STUDENT_TEMPLATE = {
    "Template Name": "EducationStudentPerformanceTemplate",

    "Subcategories": {

        "Student Profile": {
            "Student Id": lambda: str(uuid.uuid4()),
            "Full Name": lambda: fake.name(),
            "Age": lambda: random.randint(12, 25),
            "Gender": lambda: random.choice(["Male", "Female", "Other"]),
            "Grade Level": lambda: random.choice([
                "6th", "7th", "8th", "9th", "10th",
                "11th", "12th", "Undergraduate", "Postgraduate"
            ])
        },

        "Academic Scores": {
            "Math Score": lambda: random.randint(0, 100),
            "Science Score": lambda: random.randint(0, 100),
            "English Score": lambda: random.randint(0, 100),
            "SocialScience Score": lambda: random.randint(0, 100),
            "Computer Score": lambda: random.randint(0, 100),
            "Overall Percentage": lambda: round(random.uniform(40, 100), 2),
            "Average Score": lambda: round(statistics.mean([random.randint(0, 100) for _ in range(5)]), 2)
        },

        "Attendance": {
            "Total Classes": lambda: random.randint(150, 250),
            "Classes Attended": lambda: random.randint(100, 240),
            "Attendance Percentage": lambda total, attended: round(attended / total * 100, 2)
        },

        "Behavior Activity": {
            "Disciplinary Actions": lambda: random.randint(0, 3),
            "Participation In Events": lambda: random.choice(["Sports", "Debate", "ScienceClub", "Music", "None"]),
            "Sports Score": lambda: random.randint(0, 50),
            "Creativity Score": lambda: random.randint(0, 50),
            "Activity Index": lambda: round(statistics.mean([random.randint(0, 50), random.randint(0, 50)]), 2)
        },

        "Performance Metrics": {
            "StudyHoursPerWeek": lambda: random.randint(2, 40),
            "HomeworkCompletionRate": lambda: random.randint(50, 100),
            "ClassParticipationScore": lambda: random.randint(1, 10),
            "Project Grade": lambda: random.choice(["A", "B", "C", "D"]),
            "Efficiency Score": lambda: round(math.sqrt(random.uniform(1, 100)) * 10, 2)
        },

        "Timestamp Info": {
            "RecordCreatedAt": lambda: datetime.datetime.now().isoformat(),
            "LastUpdatedAt": lambda: datetime.datetime.now().isoformat(),
            "DaysSinceCreation": lambda: 0
        }
    }
}

PRODUCT_CATALOG_TEMPLATE = {
    "Template Name": "product_catalog_template",

    "Subcategories": {

        # ==============================
        # BASIC PRODUCT INFO
        # ==============================
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

            # Light math usage: rating confidence factor
            "Quality Confidence Score": lambda: round(
                math.sqrt(random.uniform(0.1, 1.0)), 3
            )
        },

        # ==============================
        # PRODUCT VARIANTS
        # ==============================
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

            # Small use of statistics (avg dimension factor)
            "Variant Score": lambda: round(
                statistics.mean([random.random() for _ in range(3)]), 3
            )
        },

        # ==============================
        # PRICING DETAILS
        # ==============================
        "Pricing": {
            "Price": lambda: round(random.uniform(100, 50000), 2),
            "Discount Percent": lambda: random.randint(0, 70),

            # Light math usage → automatic discount calculation
            "Final Price": lambda: lambda price=None, discount=None: (
                lambda base, disc: round(base - (base * disc / 100), 2)
            )(
                price if price else random.uniform(100, 50000),
                discount if discount else random.randint(0, 70)
            ),

            "Currency": lambda: random.choice(["INR", "USD", "EUR"])
        },

        # ==============================
        # STOCK & INVENTORY
        # ==============================
        "Inventory": {
            "In Stock": lambda: fake.boolean(),
            "Stock Quantity": lambda: random.randint(0, 500),
            "Warehouse Location": lambda: random.choice(
                ["Delhi", "Mumbai", "Chennai", "Bangalore", "Hyderabad"]
            ),

            # Timestamps using datetime
            "Restock Date": lambda: (
                datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 60))
            ).isoformat()
        },

        # ==============================
        # RATINGS & REVIEWS
        # ==============================
        "Ratings Reviews": {
            "Average Rating": lambda: round(random.uniform(1.0, 5.0), 2),
            "Total Reviews": lambda: random.randint(0, 50000),
            "Top Review Title": lambda: fake.sentence(),
            "Top Review Text": lambda: fake.paragraph(nb_sentences=2),

            # math + statistics for review weight
            "Review Weight Score": lambda: round(
                (random.uniform(1, 5) + math.sqrt(random.random())) / 2, 3
            )
        },

        # ==============================
        # RELEASE / TIMESTAMPS
        # ==============================
        "Timestamps": {
            "Released At": lambda: fake.iso8601(),

            # Modified timestamp using time delay simulation
            "Last Updated At": lambda: (
                datetime.datetime.now() - datetime.timedelta(
                    seconds=random.randint(60, 86400)
                )
            ).isoformat()
        }
    }
}

