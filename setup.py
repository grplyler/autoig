from setuptools import setup, find_packages

setup(
    name="autoig",
    description="Google Sheets to Instagram Post Generator",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
        "click",
        "pandas",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            "autoig = autoig.cli:cli"
        ]
    },
)