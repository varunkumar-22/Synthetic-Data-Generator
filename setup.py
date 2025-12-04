from setuptools import setup, find_packages

setup(
    name="structured_data_generator",
    version="1.0.0",
    description="A powerful CLI tool to generate realistic synthetic data for testing and development",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "faker>=8.0.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "generate-dataset=scripts.generate_dataset:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
