def main():
    print("\n=== Synthetic Data Generator CLI ===\n")

    # Step 1: Template selection
    print("Available Templates:")
    for idx, tname in enumerate(TEMPLATES.keys(), start=1):
        print(f"{idx}. {tname}")

    template_choice = input("\nSelect a template (number): ").strip()