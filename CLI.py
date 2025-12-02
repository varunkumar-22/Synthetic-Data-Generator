import random
import pandas as pd
from faker import Faker
import uuid
import time

# ---------------------------
# IMPORT YOUR TEMPLATES
# ---------------------------

from Data_Engine import USER_TEMPLATE , ECOM_TEMPLATE, FINANCIAL_TEMPLATE, HEALTHCARE_TEMPLATE, IOT_SENSOR_TEMPLATE,PRODUCT_CATALOG_TEMPLATE
from Data_Engine import NLP_TEXT_TEMPLATE, WEB_ANALYTICS_TEMPLATE,IMAGE_METADATA_TEMPLATE,EDU_STUDENT_TEMPLATE
# You can add more later

# Add all templates here (scalable for future)

TEMPLATES = {
    "USER TEMPLATE": USER_TEMPLATE,
    "ecommerce_transaction_template": ECOM_TEMPLATE,
    "financial_banking_transaction_template": FINANCIAL_TEMPLATE,
    "healthcare_medical_template": HEALTHCARE_TEMPLATE,
    "iot_sensor_template": IOT_SENSOR_TEMPLATE,
    "nlp_text_template": NLP_TEXT_TEMPLATE,
    "web_analytics_template": WEB_ANALYTICS_TEMPLATE,
    "image_metadata_template": IMAGE_METADATA_TEMPLATE,
    "education_student_performance_template": EDU_STUDENT_TEMPLATE,
    "product_catalog_template": PRODUCT_CATALOG_TEMPLATE,
}

# ---------------------------
# IMPORT YOUR GENERATOR ENGINE
# ---------------------------

from DATA_ENGINE import generate_from_template

def main():
    print(""" 
-----------------------------
🔥 SYNTHETIC DATA GENERATOR 🔥
-----------------------------""")

    # Step 1: Template selection
    print("\nAvailable Templates:\n")

    for idx, tname in enumerate(TEMPLATES.keys(), start=1):
        print(f"{idx}. {tname}\n")

    template_choice = input("\nSelect a Template (number): ").strip()

    # Validate choice
    try:
        template_index = int(template_choice) - 1
        template_name = list(TEMPLATES.keys())[template_index]
    except (ValueError, IndexError):
        print("❌ Invalid template selection!")
        return