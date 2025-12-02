try:
        template_index = int(template_choice) - 1
        template_name = list(TEMPLATES.keys())[template_index]
    except (ValueError, IndexError):
        print("❌ Invalid template selection!")
        return

    template = TEMPLATES[template_name]