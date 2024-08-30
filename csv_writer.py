import csv

file_name = "companies.csv"


def write_csv(data):
    with open(file_name, 'a', encoding='utf-8') as file:
        # Write the data to the file in semicolon-delimited format
        file.write(str(data))
