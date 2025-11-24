import random
import pandas as pd
from faker import Faker
import uuid

# ---------------------------
# IMPORT YOUR TEMPLATES
# ---------------------------

from Data_Engine import USER_TEMPLATE , ECOM_TEMPLATE, FINANCIAL_TEMPLATE, HEALTHCARE_TEMPLATE, IOT_SENSOR_TEMPLATE,PRODUCT_CATALOG_TEMPLATE
from Data_Engine import NLP_TEXT_TEMPLATE, WEB_ANALYTICS_TEMPLATE,IMAGE_METADATA_TEMPLATE,EDU_STUDENT_TEMPLATE
# You can add more later

# Add all templates here (scalable for future)
TEMPLATES = {
    "user_template": USER_TEMPLATE,
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

from Data_Engine import generate_from_template


# ---------------------------
# FLEXIBLE CLI IMPLEMENTATION
# ---------------------------

def main():
    print("\n=== Synthetic Data Generator CLI ===\n")

    # Step 1: Template selection
    print("Available Templates:")
    for idx, tname in enumerate(TEMPLATES.keys(), start=1):
        print(f"{idx}. {tname}")

    template_choice = input("\nSelect a template (number): ").strip()

    # Validate choice
    try:
        template_index = int(template_choice) - 1
        template_name = list(TEMPLATES.keys())[template_index]
    except (ValueError, IndexError):
        print("❌ Invalid template selection!")
        return

    template = TEMPLATES[template_name]

    # Step 2: Show subcategories only after selecting template
    print("\nAvailable Subcategories:")
    subcats = list(template["subcategories"].keys())
    for idx, sc in enumerate(subcats, start=1):
        print(f"{idx}. {sc}")

    selected_input = input(
        "\nEnter subcategories (comma-separated numbers): "
    ).strip()

    try:
        selected_indices = [int(x) - 1 for x in selected_input.split(",")]
        selected_subcats = [subcats[i] for i in selected_indices]
    except Exception:
        print("❌ Invalid subcategory selection!")
        return

    # Step 3: Count
    try:
        count = int(input("\nEnter number of rows to generate: ").strip())
    except ValueError:
        print("❌ Invalid count!")
        return

    # Step 4: Seed (optional)
    seed_input = input("\nEnter seed (press Enter to skip): ").strip()
    seed = int(seed_input) if seed_input else None

    # Step 5: Generate data using your generator engine
    print("\nGenerating synthetic data...")
    df = generate_from_template(template, selected_subcats, count, seed)

    # Step 6: Save output
    filename = f"{template_name}_output.csv"
    df.to_csv(filename, index=False)

    print(f"\n✅ Data generated successfully!")
    print(f"📁 Saved as: {filename}\n")


if __name__ == "__main__":
    main()