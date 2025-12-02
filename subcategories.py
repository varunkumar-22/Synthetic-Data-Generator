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