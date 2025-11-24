from faker import Faker
import random
import uuid
import pandas as pd

fake = Faker(locale="en_US")

# -------------------------------------
# USER TEMPLATE
# -------------------------------------
USER_TEMPLATE = {
    "template_name": "user_template",

    "subcategories": {

        "personal_info": {
            "full_name": lambda: fake.name(),
            "username": lambda: fake.user_name(),
            "email": lambda: fake.email(),
            "phone_number": lambda: fake.phone_number(),
            "gender": lambda: random.choice(["male", "female", "other"]),
            "date_of_birth": lambda: fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
        },

        "address": {
            "street": lambda: fake.street_address(),
            "city": lambda: fake.city(),
            "state": lambda: fake.state(),
            "country": lambda: fake.country(),
            "pincode": lambda: fake.postcode()
        },

        "account_info": {
            "account_created_at": lambda: fake.iso8601(),
            "last_login": lambda: fake.iso8601(),
            "account_status": lambda: random.choice(["Active", "Suspended", "Closed"])
        },

        "preferences": {
            "preferred_language": lambda: random.choice(["English", "Hindi", "Tamil", "Telugu", "Kannada"]),
            "preferred_currency": lambda: random.choice(["INR", "USD", "EUR"]),
            "marketing_opt_in": lambda: fake.boolean()
        },

        "device_info": {
            "device_type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "os": lambda: random.choice(["iOS", "Android", "Windows", "MacOS", "Linux"]),
            "browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}


# --------------------------------------------------------
# GENERATOR WITH COUNT SUPPORT (ID NOT PRINTED)
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

    # ❌ Remove "id" column from final visible output
    if "id" in df.columns:
        df = df.drop(columns=["id"])

    return df


# --------------------------------------------------------
# TEST RUN
# --------------------------------------------------------

# selected = [ "account_info"]
# df = generate_from_template(USER_TEMPLATE, selected, count=5, seed=42)

# print(df.to_string(index=False))



from faker import Faker
import random
import uuid
import pandas as pd

fake = Faker()

# -------------------------------------
# E-COMMERCE TRANSACTION TEMPLATE
# -------------------------------------

ECOM_TEMPLATE = {
    "template_name": "ecommerce_transaction_template",

    "subcategories": {

        # 1. Order Metadata
        "order_info": {
            "order_id": lambda: fake.uuid4(),
            "transaction_date": lambda: fake.iso8601(),
            "order_status": lambda: random.choice(["Placed", "Paid", "Shipped", "Delivered", "Cancelled", "Returned"]),
            "total_amount": lambda: round(random.uniform(150, 50000), 2),
            "currency": lambda: random.choice(["INR", "USD", "EUR"])
        },

        # 2. Customer Details
        "user_info": {
            "user_id": lambda: fake.uuid4(),
            "customer_name": lambda: fake.name(),
            "customer_email": lambda: fake.email(),
            "customer_phone": lambda: fake.phone_number()
        },

        # 3. Product Details
        "product_info": {
            "product_id": lambda: fake.uuid4(),
            "product_name": lambda: random.choice([
                "Wireless Earbuds", "Smartphone", "Laptop", "T-Shirt", "Shoes",
                "LED TV", "Bluetooth Speaker", "Backpack", "Keyboard", "Novel Book"
            ]),
            "category": lambda: random.choice([
                "Electronics", "Fashion", "Home Appliances", "Books", "Grocery",
                "Beauty", "Toys", "Sports", "Automotive", "Furniture"
            ]),
            "quantity": lambda: random.randint(1, 5),
            "price_per_unit": lambda: round(random.uniform(100, 20000), 2)
        },

        # 4. Payment Details
        "payment_info": {
            "payment_method": lambda: random.choice([
                "Credit Card", "Debit Card", "UPI", "Wallet", "COD",
                "NetBanking", "EMI", "PayLater", "Gift Card"
            ]),
            "payment_status": lambda: random.choice(["Success", "Pending", "Failed"]),
            "transaction_id": lambda: fake.uuid4()
        },

        # 5. Shipping Details
        "shipping_info": {
            "shipping_address": lambda: fake.address().replace("\n", ", "),
            "city": lambda: fake.city(),
            "state": lambda: fake.state(),
            "country": lambda: fake.country(),
            "pincode": lambda: fake.postcode(),
            "shipping_partner": lambda: random.choice(["BlueDart", "Delhivery", "Ecom Express", "FedEx", "DTDC"]),
            "shipping_status": lambda: random.choice(["Not Shipped", "In Transit", "Out for Delivery", "Delivered"])
        },

        # 6. Device Info
        "device_info": {
            "device_type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "os": lambda: random.choice(["Android", "iOS", "Windows", "MacOS"]),
            "browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}


# --------------------------------------------------------
# UNIVERSAL GENERATOR (COUNT + SEED + FORMAT + NO ID)
# --------------------------------------------------------

def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    all_rows = []

    for _ in range(count):
        generated_data = {"_internal_id": str(uuid.uuid4())}  # internal only

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    generated_data[field] = fn()

        all_rows.append(generated_data)

    df = pd.DataFrame(all_rows)

    # ❌ remove internal id from visible result
    if "_internal_id" in df.columns:
        df = df.drop(columns=["_internal_id"])

    return df


# --------------------------------------------------------
# TEST RUN
# --------------------------------------------------------

# selected = [ "shipping_info"]
# df = generate_from_template(ECOM_TEMPLATE, selected, count=30, seed=42)

# print(df.to_string(index=False))


from faker import Faker
import random
import uuid
import pandas as pd

fake = Faker()

# -----------------------------------------------------
# FINANCIAL & BANKING TRANSACTION TEMPLATE
# -----------------------------------------------------

FINANCIAL_TEMPLATE = {
    "template_name": "financial_banking_transaction_template",

    "subcategories": {

        # 1. ACCOUNT INFORMATION
        "account_info": {
            "account_id": lambda: fake.uuid4(),
            "account_type": lambda: random.choice(["Savings", "Current", "Salary", "NRE", "NRO", "Fixed Deposit"]),
            "bank_name": lambda: random.choice([
                "HDFC Bank", "ICICI Bank", "SBI", "Axis Bank", "Kotak Mahindra Bank",
                "Yes Bank", "Punjab National Bank", "Bank of Baroda"
            ]),
            "branch": lambda: fake.city(),
            "ifsc_code": lambda: "BANK" + str(random.randint(10000, 99999)),
            "account_holder_name": lambda: fake.name()
        },

        # 2. TRANSACTION DETAILS
        "transaction_info": {
            "transaction_id": lambda: fake.uuid4(),
            "transaction_date": lambda: fake.iso8601(),
            "transaction_type": lambda: random.choice([
                "Deposit", "Withdrawal", "Online Transfer", "UPI Payment", "Card Payment",
                "Loan EMI", "Interest Credit", "Service Charge"
            ]),
            "amount": lambda: round(random.uniform(100, 200000), 2),
            "currency": lambda: random.choice(["INR", "USD", "EUR"]),
            "transaction_status": lambda: random.choice(["Success", "Pending", "Failed"])
        },

        # 3. CUSTOMER INFO
        "customer_info": {
            "customer_id": lambda: fake.uuid4(),
            "customer_name": lambda: fake.name(),
            "email": lambda: fake.email(),
            "phone_number": lambda: fake.phone_number(),
            "PAN_number": lambda: "".join([chr(random.randint(65, 90)) for _ in range(5)]) +
                                   str(random.randint(1000, 9999)) +
                                   chr(random.randint(65, 90)),
            "aadhaar_last4": lambda: random.randint(1000, 9999)
        },

        # 4. CARD DETAILS (OPTIONAL)
        "card_info": {
            "card_type": lambda: random.choice(["Debit Card", "Credit Card", "Prepaid Card"]),
            "card_network": lambda: random.choice(["Visa", "Mastercard", "RuPay", "American Express"]),
            "card_last4": lambda: random.randint(1000, 9999),
            "card_issuer_bank": lambda: random.choice([
                "SBI", "HDFC", "ICICI", "Axis Bank", "Kotak", "Punjab National Bank"
            ])
        },

        # 5. LOAN DETAILS (OPTIONAL)
        "loan_info": {
            "loan_id": lambda: fake.uuid4(),
            "loan_type": lambda: random.choice(["Home Loan", "Personal Loan", "Car Loan", "Education Loan"]),
            "loan_amount": lambda: round(random.uniform(50000, 2500000), 2),
            "interest_rate": lambda: round(random.uniform(6.5, 14.0), 2),
            "emi_amount": lambda: round(random.uniform(2000, 50000), 2)
        },

        # 6. DEVICE INFORMATION (FOR ONLINE TRANSACTIONS)
        "device_info": {
            "device_type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "os": lambda: random.choice(["Android", "iOS", "Windows", "MacOS", "Linux"]),
            "browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}

# --------------------------------------------------------
# UNIVERSAL GENERATOR (COUNT + SEED + PANDAS + NO ID)
# --------------------------------------------------------

def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    all_rows = []

    for _ in range(count):
        generated_data = {"_internal_id": str(uuid.uuid4())}  # internal only

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    generated_data[field] = fn()

        all_rows.append(generated_data)

    df = pd.DataFrame(all_rows)

    # Hide internal ID from output
    if "_internal_id" in df.columns:
        df = df.drop(columns=["_internal_id"])

    return df


# --------------------------------------------------------
# TEST RUN
# --------------------------------------------------------

# selected = [ "card_info"]
# df = generate_from_template(FINANCIAL_TEMPLATE, selected, count=5, seed=100)

# print(df.to_string(index=False))



from faker import Faker
import random
import uuid
import pandas as pd

fake = Faker()

# -----------------------------------------------------
# HEALTHCARE & MEDICAL DATA TEMPLATE
# -----------------------------------------------------

HEALTHCARE_TEMPLATE = {
    "template_name": "healthcare_medical_template",

    "subcategories": {

        # 1. PATIENT INFORMATION
        "patient_info": {
            "patient_id": lambda: fake.uuid4(),
            "full_name": lambda: fake.name(),
            "age": lambda: random.randint(1, 95),
            "gender": lambda: random.choice(["male", "female", "other"]),
            "blood_group": lambda: random.choice(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]),
            "contact_number": lambda: fake.phone_number(),
            "email": lambda: fake.email(),
            "address": lambda: fake.address().replace("\n", ", ")
        },

        # 2. MEDICAL RECORD DETAILS
        "medical_record": {
            "record_id": lambda: fake.uuid4(),
            "diagnosis": lambda: random.choice([
                "Hypertension", "Diabetes", "Asthma", "Migraine", "Allergy",
                "Arthritis", "Viral Infection", "Flu", "Back Pain", "Cholesterol"
            ]),
            "symptoms": lambda: random.choice([
                "Fever, Cough, Fatigue",
                "Headache, Nausea",
                "Chest Pain, Dizziness",
                "Joint Pain, Swelling",
                "Shortness of Breath"
            ]),
            "severity": lambda: random.choice(["Mild", "Moderate", "Severe", "Critical"]),
            "diagnosis_date": lambda: fake.date()
        },

        # 3. DOCTOR DETAILS
        "doctor_info": {
            "doctor_id": lambda: fake.uuid4(),
            "doctor_name": lambda: fake.name(),
            "specialization": lambda: random.choice([
                "General Physician", "Cardiologist", "Neurologist",
                "Dermatologist", "Pediatrician", "Orthopedic",
                "Gynecologist", "ENT Specialist"
            ]),
            "hospital_name": lambda: random.choice([
                "Apollo Hospital", "Fortis Hospital", "AIIMS", "Max Healthcare",
                "Narayana Health", "Care Hospitals", "KIMS Hospitals"
            ])
        },

        # 4. APPOINTMENT DETAILS
        "appointment_info": {
            "appointment_id": lambda: fake.uuid4(),
            "appointment_date": lambda: fake.iso8601(),
            "appointment_status": lambda: random.choice(["Scheduled", "Completed", "Cancelled", "No-Show"]),
            "consultation_type": lambda: random.choice(["In-Person", "Online Video", "Telephonic"])
        },

        # 5. PRESCRIPTION DETAILS
        "prescription_info": {
            "prescription_id": lambda: fake.uuid4(),
            "medicine_name": lambda: random.choice([
                "Paracetamol", "Ibuprofen", "Amoxicillin", "Cetirizine",
                "Vitamin D", "Metformin", "Aspirin", "Omeprazole"
            ]),
            "dosage": lambda: random.choice(["1 tablet daily", "2 tablets daily", "1 tablet after meals"]),
            "duration_days": lambda: random.randint(3, 30)
        },

        # 6. BILLING / PAYMENT INFO
        "billing_info": {
            "invoice_id": lambda: fake.uuid4(),
            "consultation_fee": lambda: random.randint(300, 2000),
            "medicine_charges": lambda: random.randint(50, 5000),
            "lab_test_charges": lambda: random.randint(100, 8000),
            "total_bill": lambda: random.randint(500, 15000),
            "payment_method": lambda: random.choice(["Cash", "Credit Card", "UPI", "Insurance", "Wallet"]),
            "payment_status": lambda: random.choice(["Paid", "Pending", "Failed"])
        },

        # 7. DEVICE INFO (for telemedicine)
        "device_info": {
            "device_type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "os": lambda: random.choice(["Android", "iOS", "Windows", "MacOS"]),
            "browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}


# --------------------------------------------------------
# UNIVERSAL GENERATOR (COUNT + SEED + NO INTERNAL ID)
# --------------------------------------------------------

def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    all_rows = []

    for _ in range(count):
        generated_data = {"_internal_id": str(uuid.uuid4())}  # internal only

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    generated_data[field] = fn()

        all_rows.append(generated_data)

    df = pd.DataFrame(all_rows)

    # Hide internal ID from output
    if "_internal_id" in df.columns:
        df = df.drop(columns=["_internal_id"])

    return df


# --------------------------------------------------------
# TEST RUN
# --------------------------------------------------------

# selected = ["patient_info"]
# df = generate_from_template(HEALTHCARE_TEMPLATE, selected, count=30, seed=50)

# print(df.to_string(index=False))



from faker import Faker
import random
import uuid
import pandas as pd
import math
import statistics

fake = Faker()

# ---------------------------------------------------------
#  IOT SENSOR DATA TEMPLATE
# ---------------------------------------------------------
IOT_SENSOR_TEMPLATE = {
    "template_name": "iot_sensor_template",

    "subcategories": {

        "device_info": {
            "device_id": lambda: f"DEV-{fake.random_int(1000, 9999)}",
            "device_type": lambda: random.choice([
                "temperature_sensor", "humidity_sensor", "motion_detector",
                "air_quality_monitor", "gps_tracker", "power_meter"
            ]),
            "firmware_version": lambda: f"{fake.random_int(1,3)}.{fake.random_int(0,9)}.{fake.random_int(0,9)}",
            "manufacturer": lambda: random.choice(["Bosch", "Siemens", "Honeywell", "Xiaomi", "Philips"])
        },

        "location_data": {
            "latitude": lambda: fake.latitude(),
            "longitude": lambda: fake.longitude(),
            "altitude_meters": lambda: round(random.uniform(5, 2000), 2),
            "zone": lambda: random.choice(["Zone-A", "Zone-B", "Zone-C"])
        },

        "sensor_readings": {
            "temperature_c": lambda: round(random.uniform(15.0, 45.0), 2),
            "humidity_percent": lambda: round(random.uniform(20.0, 90.0), 2),
            "air_quality_index": lambda: fake.random_int(10, 300),
            "co2_ppm": lambda: fake.random_int(350, 2000),
            "motion_detected": lambda: fake.boolean()
        },

        "network_data": {
            "signal_strength_dbm": lambda: fake.random_int(-100, -40),
            "connection_type": lambda: random.choice(["WiFi", "LTE", "LoRaWAN", "ZigBee"]),
            "ip_address": lambda: fake.ipv4()
        },

        "battery_power": {
            "battery_level_percent": lambda: fake.random_int(10, 100),
            "battery_health": lambda: random.choice(["Good", "Moderate", "Weak"]),
            "charging_status": lambda: random.choice(["Charging", "Not Charging"])
        },

        "timestamp_info": {
            "timestamp": lambda: fake.iso8601(),
            "last_maintenance": lambda: fake.date_this_year().isoformat()
        }
    }
}


# ---------------------------------------------------------
#  ULTRA-SIMPLE GENERATOR (supports seed + count)
# ---------------------------------------------------------
def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    rows = []

    for _ in range(count):
        row = {}  # no template id printed

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    row[field] = fn()

        rows.append(row)

    # pandas formatting
    df = pd.DataFrame(rows)
    return df


# ---------------------------------------------------------
#  TEST RUN
# ---------------------------------------------------------
# selected = ["device_info"]
# df = generate_from_template(IOT_SENSOR_TEMPLATE, selected, count=5, seed=99)

# print(df.to_string(index=False))


from faker import Faker
import random
import uuid
import pandas as pd
import math
import statistics

fake = Faker()

# ---------------------------------------------------------
#  NLP / TEXT CORPUS TEMPLATE
# ---------------------------------------------------------
NLP_TEXT_TEMPLATE = {
    "template_name": "nlp_text_template",

    "subcategories": {

        "basic_text": {
            "sentence": lambda: fake.sentence(),
            "short_paragraph": lambda: fake.paragraph(nb_sentences=3),
            "long_paragraph": lambda: fake.paragraph(nb_sentences=7),
            "word": lambda: fake.word(),
            "keywords": lambda: ", ".join(fake.words(nb=5))
        },

        "document_metadata": {
            "title": lambda: fake.sentence(nb_words=4),
            "author": lambda: fake.name(),
            "published_year": lambda: fake.year(),
            "document_type": lambda: random.choice([
                "article", "blog", "research_paper", "report", "review", "story"
            ])
        },

        "nlp_annotations": {
            "language": lambda: random.choice(["en", "hi", "ta", "fr", "es"]),
            "sentiment": lambda: random.choice(["positive", "negative", "neutral"]),
            "emotion": lambda: random.choice(["joy", "anger", "sadness", "fear", "neutral"]),
            "toxicity_flag": lambda: fake.boolean(),
            "reading_level": lambda: random.choice(["easy", "moderate", "complex"])
        },

        "synthetic_ner_data": {
            "person_name": lambda: fake.name(),
            "location_name": lambda: fake.city(),
            "organization": lambda: fake.company(),
            "misc_entity": lambda: random.choice(["COVID-19", "AI", "Climate", "Blockchain", "Quantum"])
        },

        "text_stats": {
            "word_count": lambda: fake.random_int(10, 300),
            "char_count": lambda: fake.random_int(50, 1200),
            "avg_word_length": lambda: round(random.uniform(3.5, 7.5), 2),
            "unique_words": lambda: fake.random_int(5, 80)
        },

        "timestamp_info": {
            "created_at": lambda: fake.iso8601(),
            "updated_at": lambda: fake.iso8601()
        }
    }
}



# ---------------------------------------------------------
#  ULTRA-SIMPLE GENERATOR (supports seed + count)
# ---------------------------------------------------------
def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    rows = []

    for _ in range(count):
        row = {}

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    row[field] = fn()

        rows.append(row)

    return pd.DataFrame(rows)



# ---------------------------------------------------------
#  TEST RUN
# ---------------------------------------------------------
# selected = ["text_stats"]
# df = generate_from_template(NLP_TEXT_TEMPLATE, selected, count=5, seed=21)

# print(df.to_string(index=False))



# ---------------------------------------------------------
#  WEB ANALYTICS TEMPLATE
# ---------------------------------------------------------
WEB_ANALYTICS_TEMPLATE = {
    "template_name": "web_analytics_template",

    "subcategories": {

        # ==============================
        # USER SESSION INFO
        # ==============================
        "session_info": {
            "session_id": lambda: str(uuid.uuid4()),
            "user_id": lambda: fake.uuid4(),
            "session_start": lambda: fake.iso8601(),
            "session_end": lambda: fake.iso8601(),
            "session_duration_sec": lambda: random.randint(5, 3600),
            "is_new_user": lambda: fake.boolean()
        },

        # ==============================
        # PAGE VIEW METRICS
        # ==============================
        "page_metrics": {
            "page_url": lambda: fake.uri(),
            "referrer_url": lambda: random.choice([fake.uri(), None]),
            "page_title": lambda: fake.sentence(nb_words=4),
            "time_on_page_sec": lambda: random.randint(1, 900),
            "scroll_depth_percent": lambda: random.randint(10, 100),
            "interaction": lambda: random.choice(["click", "scroll", "hover", "input", "none"])
        },

        # ==============================
        # TRAFFIC SOURCE
        # ==============================
        "traffic_source": {
            "source": lambda: random.choice(["Direct", "Organic", "Paid", "Referral", "Social"]),
            "medium": lambda: random.choice(["none", "cpc", "email", "banner", "social"]),
            "campaign": lambda: random.choice(["summer_sale", "new_launch", "retargeting", "none"]),
            "keyword": lambda: random.choice([fake.word(), None])
        },

        # ==============================
        # DEVICE & BROWSER INFO
        # ==============================
        "device_info": {
            "device_type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"]),
            "os": lambda: random.choice(["Windows", "MacOS", "Android", "iOS", "Linux"]),
            "screen_resolution": lambda: random.choice([
                "1920x1080", "1366x768", "1536x864", "1280x720", "1440x900"
            ])
        },

        # ==============================
        # LOCATION / GEO DATA
        # ==============================
        "geo_data": {
            "ip_address": lambda: fake.ipv4_public(),
            "country": lambda: fake.country(),
            "city": lambda: fake.city(),
            "timezone": lambda: fake.timezone()
        },

        # ==============================
        # PERFORMANCE DATA
        # ==============================
        "performance": {
            "page_load_time_ms": lambda: random.randint(200, 5000),
            "dns_lookup_ms": lambda: random.randint(10, 300),
            "ttfb_ms": lambda: random.randint(50, 1200),  # Time To First Byte
            "total_resources_loaded": lambda: random.randint(5, 100),
            "js_errors": lambda: random.randint(0, 10)
        }
    }
}


# ---------------------------------------------------------
# ULTRA-SIMPLE GENERATOR (seed + count)
# ---------------------------------------------------------
def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    rows = []

    for _ in range(count):
        row = {}

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    row[field] = fn()

        rows.append(row)

    return pd.DataFrame(rows)


# ---------------------------------------------------------
# TEST RUN
# ---------------------------------------------------------
# selected = [ "traffic_source"]
# df = generate_from_template(WEB_ANALYTICS_TEMPLATE, selected, count=5, seed=99)

# print(df.to_string(index=False))





# ---------------------------------------------------------
#  IMAGE METADATA TEMPLATE
# ---------------------------------------------------------
IMAGE_METADATA_TEMPLATE = {
    "template_name": "image_metadata_template",

    "subcategories": {

        # ==============================
        # BASIC IMAGE INFO
        # ==============================
        "basic_info": {
            "image_id": lambda: str(uuid.uuid4()),
            "file_name": lambda: fake.file_name(category="image"),
            "file_format": lambda: random.choice(["jpg", "jpeg", "png", "webp", "tiff"]),
            "file_size_kb": lambda: random.randint(50, 15000),   # 50 KB – 15 MB
            "color_mode": lambda: random.choice(["RGB", "RGBA", "CMYK", "Grayscale"])
        },

        # ==============================
        # DIMENSIONS & QUALITY
        # ==============================
        "dimensions": {
            "width_px": lambda: random.randint(256, 8000),
            "height_px": lambda: random.randint(256, 8000),
            "aspect_ratio": lambda: random.choice(["1:1", "4:3", "16:9", "21:9", "3:2"]),
            "dpi": lambda: random.choice([72, 96, 150, 300])
        },

        # ==============================
        # CAMERA / EXIF DATA
        # ==============================
        "camera_exif": {
            "camera_make": lambda: random.choice(["Canon", "Nikon", "Sony", "Fujifilm", "Apple", "Samsung"]),
            "camera_model": lambda: fake.word(),
            "lens_model": lambda: random.choice(["18-55mm", "24-70mm", "50mm", "70-200mm", None]),
            "focal_length_mm": lambda: random.randint(10, 200),
            "aperture": lambda: random.choice(["f/1.8", "f/2.0", "f/2.8", "f/4", "f/5.6"]),
            "iso": lambda: random.choice([100, 200, 400, 800, 1600, 3200]),
            "exposure_time": lambda: random.choice(["1/50", "1/100", "1/200", "1/500"])
        },

        # ==============================
        # GEOLOCATION INFO
        # ==============================
        "geolocation": {
            "latitude": lambda: float(fake.latitude()),
            "longitude": lambda: float(fake.longitude()),
            "country": lambda: fake.country(),
            "city": lambda: fake.city()
        },

        # ==============================
        # CONTENT TAGS / LABELS
        # ==============================
        "tags_labels": {
            "primary_label": lambda: random.choice([
                "person", "animal", "landscape", "food", "vehicle", "object", "logo"
            ]),
            "secondary_labels": lambda: ", ".join(fake.words(nb=3)),
            "confidence_score": lambda: round(random.uniform(0.5, 1.0), 3)
        },

        # ==============================
        # TIMESTAMP INFO
        # ==============================
        "timestamp_info": {
            "created_at": lambda: fake.iso8601(),
            "uploaded_at": lambda: fake.iso8601(),
            "last_modified_at": lambda: fake.iso8601()
        }
    }
}



# ---------------------------------------------------------
# ULTRA-SIMPLE GENERATOR (seed + count)
# ---------------------------------------------------------
def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    rows = []

    for _ in range(count):
        row = {}

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    row[field] = fn()

        rows.append(row)

    return pd.DataFrame(rows)



# ---------------------------------------------------------
# TEST RUN
# ---------------------------------------------------------
# selected = ["basic_info"]
# df = generate_from_template(IMAGE_METADATA_TEMPLATE, selected, count=5, seed=10)

# print(df.to_string(index=False))


from faker import Faker
import random
import uuid
import pandas as pd
import math
import statistics

fake = Faker()

# ---------------------------------------------------------
#  EDUCATION / STUDENT PERFORMANCE TEMPLATE
# ---------------------------------------------------------
EDU_STUDENT_TEMPLATE = {
    "template_name": "education_student_performance_template",

    "subcategories": {

        # ==============================
        # BASIC STUDENT PROFILE
        # ==============================
        "student_profile": {
            "student_id": lambda: fake.uuid4(),
            "full_name": lambda: fake.name(),
            "age": lambda: random.randint(12, 25),
            "gender": lambda: random.choice(["male", "female", "other"]),
            "grade_level": lambda: random.choice([
                "6th", "7th", "8th", "9th", "10th",
                "11th", "12th", "Undergraduate", "Postgraduate"
            ])
        },

        # ==============================
        # ACADEMIC SCORES
        # ==============================
        "academic_scores": {
            "math_score": lambda: random.randint(0, 100),
            "science_score": lambda: random.randint(0, 100),
            "english_score": lambda: random.randint(0, 100),
            "social_science_score": lambda: random.randint(0, 100),
            "computer_score": lambda: random.randint(0, 100),
            "overall_percentage": lambda: round(random.uniform(40, 100), 2)
        },

        # ==============================
        # ATTENDANCE DATA
        # ==============================
        "attendance": {
            "total_classes": lambda: random.randint(150, 250),
            "classes_attended": lambda: random.randint(100, 240),
            "attendance_percentage": lambda: round(random.uniform(50, 100), 2)
        },

        # ==============================
        # BEHAVIOR & EXTRACURRICULAR
        # ==============================
        "behavior_activity": {
            "disciplinary_actions": lambda: random.randint(0, 3),
            "participation_in_events": lambda: random.choice([
                "sports", "debate", "science_club", "music", "none"
            ]),
            "sports_score": lambda: random.randint(0, 50),
            "creativity_score": lambda: random.randint(0, 50)
        },

        # ==============================
        # PERFORMANCE METRICS
        # ==============================
        "performance_metrics": {
            "study_hours_per_week": lambda: random.randint(2, 40),
            "homework_completion_rate": lambda: random.randint(50, 100),
            "class_participation_score": lambda: random.randint(1, 10),
            "project_grade": lambda: random.choice(["A", "B", "C", "D"])
        },

        # ==============================
        # TIMESTAMP INFO
        # ==============================
        "timestamp_info": {
            "record_created_at": lambda: fake.iso8601(),
            "last_updated_at": lambda: fake.iso8601()
        }
    }
}



# ---------------------------------------------------------
# ULTRA-SIMPLE GENERATOR (seed + count)
# ---------------------------------------------------------
def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    rows = []

    for _ in range(count):
        row = {}

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    row[field] = fn()

        rows.append(row)

    return pd.DataFrame(rows)



# ---------------------------------------------------------
# TEST RUN
# ---------------------------------------------------------
# selected = [ "academic_scores"]
# df = generate_from_template(EDU_STUDENT_TEMPLATE, selected, count=5, seed=101)

# print(df.to_string(index=False))


from faker import Faker
import random
import uuid
import pandas as pd
import math
import statistics

fake = Faker()

# ---------------------------------------------------------
#  PRODUCT CATALOG TEMPLATE
# ---------------------------------------------------------
PRODUCT_CATALOG_TEMPLATE = {
    "template_name": "product_catalog_template",

    "subcategories": {

        # ==============================
        # BASIC PRODUCT INFO
        # ==============================
        "basic_info": {
            "product_id": lambda: str(uuid.uuid4()),
            "product_name": lambda: fake.catch_phrase(),
            "category": lambda: random.choice([
                "Electronics", "Fashion", "Home Appliances", "Kitchen", "Books",
                "Furniture", "Beauty", "Groceries", "Automotive", "Sports",
                "Toys", "Pet Supplies", "Healthcare"
            ]),
            "brand": lambda: fake.company(),
            "description": lambda: fake.paragraph(nb_sentences=3)
        },

        # ==============================
        # PRODUCT VARIANTS
        # ==============================
        "variants": {
            "color": lambda: random.choice([
                "Red", "Blue", "Black", "White", "Green", "Yellow", "Grey", None
            ]),
            "size": lambda: random.choice([
                "S", "M", "L", "XL", "XXL", "32GB", "64GB", "128GB", None
            ]),
            "material": lambda: random.choice([
                "Plastic", "Steel", "Cotton", "Leather", "Metal", None
            ]),
            "model_number": lambda: fake.bothify("MDL-###-??")
        },

        # ==============================
        # PRICING DETAILS
        # ==============================
        "pricing": {
            "price": lambda: round(random.uniform(100, 50000), 2),
            "discount_percent": lambda: random.randint(0, 70),
            "final_price": lambda: round(random.uniform(50, 45000), 2),
            "currency": lambda: random.choice(["INR", "USD", "EUR"])
        },

        # ==============================
        # STOCK & INVENTORY
        # ==============================
        "inventory": {
            "in_stock": lambda: fake.boolean(),
            "stock_quantity": lambda: random.randint(0, 500),
            "warehouse_location": lambda: random.choice(["Delhi", "Mumbai", "Chennai", "Bangalore", "Hyderabad"]),
            "restock_date": lambda: fake.iso8601()
        },

        # ==============================
        # RATINGS & REVIEWS
        # ==============================
        "ratings_reviews": {
            "average_rating": lambda: round(random.uniform(1.0, 5.0), 2),
            "total_reviews": lambda: random.randint(0, 50000),
            "top_review_title": lambda: fake.sentence(),
            "top_review_text": lambda: fake.paragraph(nb_sentences=2)
        },

        # ==============================
        # RELEASE / TIMESTAMPS
        # ==============================
        "timestamps": {
            "released_at": lambda: fake.iso8601(),
            "last_updated_at": lambda: fake.iso8601()
        }
    }
}



# ---------------------------------------------------------
# ULTRA-SIMPLE GENERATOR (seed + count)
# ---------------------------------------------------------
def generate_from_template(template, selected_subcats, count=1, seed=None):
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    rows = []

    for _ in range(count):
        row = {}

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    row[field] = fn()

        rows.append(row)

    return pd.DataFrame(rows)



# ---------------------------------------------------------
# TEST RUN
# ---------------------------------------------------------
# selected = [ "inventory"]
# df = generate_from_template(PRODUCT_CATALOG_TEMPLATE, selected, count=10000, seed=2024)

# print(df.to_string(index=False))
