# Structured Data Generator - Project Structure

## 📁 Project Organization

```
structured_data_generator/
│
├── README.md                          # Project overview, installation, usage
├── setup.py                           # For packaging and dependencies
├── pyproject.toml                     # Modern Python packaging
├── requirements.txt                   # Required Python packages
├── LICENSE                            # MIT License
│
├── data/                              # Sample input/output datasets
│   ├── raw/                           # Raw input data
│   └── generated/                     # Generated output data
│
├── structured_data_generator/         # Main source code package
│   ├── __init__.py
│   │
│   ├── core/                          # Core data generation logic
│   │   ├── __init__.py
│   │   ├── generators.py              # All templates and generation engine
│   │   ├── constraints.py             # Enforce ranges, uniqueness, correlations
│   │   └── utils.py                   # Helper functions, seed management
│   │
│   ├── io/                            # Input/output handling
│   │   ├── __init__.py
│   │   ├── csv_handler.py             # CSV read/write
│   │   └── json_handler.py            # JSON read/write
│   │
│   ├── profiling/                     # Data profiling and summary statistics
│   │   ├── __init__.py
│   │   └── profiler.py                # Generate dataset profiles
│   │
│   └── config/                        # Configuration management
│       ├── __init__.py
│       └── default_config.py          # Default parameters, distributions, seed
│
├── tests/                             # Unit tests
│   ├── __init__.py
│   ├── test_generators.py             # Test data generation
│   ├── test_constraints.py            # Test constraint enforcement
│   ├── test_io.py                     # Test I/O operations
│   └── test_profiler.py               # Test profiling functionality
│
├── scripts/                           # CLI or automation scripts
│   ├── __init__.py
│   ├── generate_dataset.py            # Main CLI for generating datasets
│   └── profile_dataset.py             # CLI for profiling datasets
│
└── examples/                          # Example notebooks
    ├── numeric_example.ipynb          # Numeric data generation examples
    ├── categorical_example.ipynb      # Categorical data examples
    └── timeseries_example.ipynb       # Time series data examples
```

## 🚀 Installation

### Option 1: Development Mode (Recommended for development)

```bash
# Clone or navigate to the project directory
cd structured_data_generator

# Install in editable mode
pip install -e .
```

### Option 2: Regular Installation

```bash
pip install .
```

### Option 3: Install from requirements.txt

```bash
pip install -r requirements.txt
```

## 📖 Usage

### Using the CLI

```bash
# Run the interactive CLI
python scripts/generate_dataset.py

# Profile an existing dataset
python scripts/profile_dataset.py data/generated/my_data.csv
```

### Using as a Python Module

```python
from structured_data_generator.core.generators import (
    USER_TEMPLATE, 
    ECOM_TEMPLATE,
    generate_from_template
)

# Generate user data
data = generate_from_template(
    USER_TEMPLATE,
    ["Personal Info", "Address"],
    count=100,
    seed=42
)

# Save to CSV
from structured_data_generator.io.csv_handler import save_to_csv
save_to_csv(data, "users.csv")
```

### Using I/O Handlers

```python
from structured_data_generator.io.csv_handler import save_to_csv, load_from_csv
from structured_data_generator.io.json_handler import save_to_json, load_from_json

# Save data
save_to_csv(dataframe, "output.csv")
save_to_json(dataframe, "output.json")

# Load data
df_csv = load_from_csv("output.csv")
df_json = load_from_json("output.json")
```

### Using Profiler

```python
from structured_data_generator.profiling.profiler import generate_profile, print_profile

# Generate and print profile
profile = generate_profile(dataframe)
print_profile(profile)
```

## 🧪 Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_generators

# Run with verbose output
python -m unittest discover tests -v
```

## 📊 Available Templates

1. **USER_TEMPLATE** - User profiles and account information
2. **ECOM_TEMPLATE** - E-commerce transactions
3. **FINANCIAL_TEMPLATE** - Banking and financial data
4. **HEALTHCARE_TEMPLATE** - Medical records and patient data
5. **IOT_SENSOR_TEMPLATE** - IoT sensor readings
6. **NLP_TEXT_TEMPLATE** - Text and NLP data
7. **WEB_ANALYTICS_TEMPLATE** - Website analytics data
8. **IMAGE_METADATA_TEMPLATE** - Image metadata
9. **EDU_STUDENT_TEMPLATE** - Student academic records
10. **PRODUCT_CATALOG_TEMPLATE** - Product catalog data

## 🔧 Configuration

Edit `structured_data_generator/config/default_config.py` to customize:

- Default locale
- Default number of rows
- CSV/JSON export settings
- Random seed behavior

## 📝 Code Migration Notes

### What Changed?

1. **Original Structure:**
   - `CLI.py` - Main CLI script
   - `DATA_ENGINE.py` - All templates and generation logic

2. **New Structure:**
   - Code split into logical modules
   - Proper package structure with `__init__.py` files
   - Separate modules for I/O, profiling, configuration
   - Unit tests added
   - Example notebooks added
   - Proper packaging with `setup.py` and `pyproject.toml`

### Import Changes

**Old way:**
```python
from DATA_ENGINE import USER_TEMPLATE, generate_from_template
```

**New way:**
```python
from structured_data_generator.core.generators import USER_TEMPLATE, generate_from_template
```

### Running the CLI

**Old way:**
```bash
python CLI.py
```

**New way:**
```bash
python scripts/generate_dataset.py
```

## 🎯 Benefits of New Structure

1. **Modularity** - Code organized into logical modules
2. **Reusability** - Easy to import and use in other projects
3. **Testability** - Unit tests for all components
4. **Maintainability** - Clear separation of concerns
5. **Scalability** - Easy to add new features
6. **Professional** - Follows Python packaging best practices
7. **Documentation** - Better organized with examples

## 🤝 Contributing

To add new templates:

1. Edit `structured_data_generator/core/generators.py`
2. Add your template following the existing pattern
3. Export it in `structured_data_generator/core/__init__.py`
4. Add tests in `tests/test_generators.py`
5. Update documentation

## 📚 Additional Resources

- See `examples/` for Jupyter notebook examples
- See `tests/` for usage examples in tests
- See original `README.md` for detailed template documentation

## ⚠️ Backward Compatibility

The original `CLI.py` and `DATA_ENGINE.py` files are still present for backward compatibility. However, it's recommended to use the new structured approach for all new development.

## 🐛 Troubleshooting

### ModuleNotFoundError

If you get `ModuleNotFoundError: No module named 'structured_data_generator'`:

```bash
# Install the package in development mode
pip install -e .
```

### Import Errors

Make sure you're using the correct import paths:

```python
from structured_data_generator.core.generators import ...
```

Not:

```python
from DATA_ENGINE import ...  # Old way
```

## 📄 License

MIT License - See LICENSE file for details
