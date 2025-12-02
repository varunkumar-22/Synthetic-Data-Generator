try:
    count = int(input("\nEnter number of rows to generate: ").strip())
except ValueError:
    print("❌ Invalid count!")
    return
