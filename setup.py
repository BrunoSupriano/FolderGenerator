from setuptools import setup, find_packages

setup(
    name="csv_xlsx_folder_creator",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl"
    ],
    entry_points={
        'console_scripts': [
            'csv_xlsx_folder_creator=csv_xlsx_folder_creator:main'
        ]
    },
    include_package_data=True,
    description="A tool to create folders based on CSV/XLSX column values",
    author="Bruno Supriano",
    author_email="brunosupriano@hotmail.com",
)