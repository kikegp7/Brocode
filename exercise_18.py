# Read files(txt, json, csv)

import json

file_path = "C:/Users/luis_/OneDrive/Escritorio/Archivos ejemplo python/example.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)

except FileNotFoundError:
    print("That file was not found.")

except PermissionError:
    print("You don't have the permission to read that file.")



import csv

file_path = "C:/Users/luis_/OneDrive/Escritorio/Archivos ejemplo python/csv_example.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)

except FileNotFoundError:
    print("That file was not found.")

except PermissionError:
    print("You don't have the permission to read that file.")