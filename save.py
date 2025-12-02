filename = f"{template_name}_output.csv"
df.to_csv(filename, index=False)

print(f"\n✅ Data generated successfully!")
print(f"📁 Saved as: {filename}\n")


if __name__ == "__main__":
    main()
