from setuptools import setup, find_packages

setup(
    name="threat_detector",
    version="1.0.0",
    description="AI-powered cybersecurity threat detection system",
    author="Corey",
    author_email="corey@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "flask",
        "plotly",
        "snowflake-connector-python",
        "pyyaml",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "threat-detector=main:run_pipeline"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)


# Install locally
pip install -e .

# Run from CLI
threat-detector
