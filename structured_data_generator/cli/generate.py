import pandas as pd
import time


from structured_data_generator.templates import TEMPLATES
from structured_data_generator.engine import generate_from_template


def main():
    print(""" 
-----------------------------
  SYNTHETIC DATA GENERATOR 
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
    
    template = TEMPLATES[template_name]

    # Step 2: Show subcategories only after selecting template
    print("\nAvailable Subcategories:")
    subcats = list(template["subcategories"].keys())
    for idx, sc in enumerate(subcats, start=1):
        print(f"{idx}. {sc}")

    selected_input = input(
        "\nEnter Subcategories (comma-separated numbers): "
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
    seed_input = input("\nEnter Seed (press Enter to skip): ").strip()
    seed = int(seed_input) if seed_input else None

    # Step 5: Generate data using your generator engine
    print("\nGenerating Synthetic Data...")
    start=time.time()
    data = generate_from_template(template, selected_subcats, count, seed)
    end=time.time()
    
    df=pd.DataFrame(data)
    
    print("\n✅ DATA  GENERATED SUCCESSFULLY!")
    print("==============================")
    print("           SUMMARY          \n")
    print(f"* Template: {template_name}")
    print(f"⏱ Time Taken: {end - start:.2f} seconds")
    print(f"* Rows Generated: {count}")
    print(f"* Columns Generated: {len(df.columns)}")
    print(f"* Seed: {seed_input}")
    print("==============================")
    
    # 6. Files export and data preview
    print("\nSelect what you want to do next:")
    print("1. Preview data (first 5 rows)")
    print("2. Save as CSV")
    print("3. Save as JSON")
    print("4. Exit\n")

    user_input = input("Enter options (comma-separated): ")

    choices = [c.strip() for c in user_input.split(",")]

    if "1" in choices:
        print("\n---- DATA PREVIEW (top 5 rows) ----")
        print(f"{df.head().to_string(index=False)}\n")

    if "2" in choices:
        file_name_input= input("Enter CSV file name: ")
        file_name= f"{file_name_input}.csv"
        df.to_csv(file_name, index=False)
        print(f"✔ CSV saved as {file_name}\n")

    if "3" in choices:
        file_name_input = input("Enter JSON file name: ")
        file_name = f"{file_name_input}.json"
        df.to_json(file_name, orient="records", indent=4)
        print(f"✔ JSON saved as {file_name}\n")

    if "4" in choices:
        print("Exiting...\n")


        print("\nThank you for using Synthetic Data Generator!")

if __name__ == "__main__":
    main()




