# Handling files

import json

employess = {"name":"Luis",
             "age": 31,
             "trabajo":"programador web"}

txt_data = "Probando a manipular archivos de texto"

file_path = "C:/Users/luis_/OneDrive/Escritorio/Archivos ejemplo python/example.json"

with open(file_path, "w") as file:
    json.dump(employess,file, indent=4)
    print(f"json file {file_path} was created.")


# Resumen: Cualquier diccionario o todo lo que use llaves pares son excelente para manejar con json

import csv

employess = [["Name", "Age", "Job"],
             ["Luis", 31, "WebDepeloper"],
             ["Ramon", 30, "Engineer"],
             ["Eduardo", 30, "Engineer"]]

file_path = "C:/Users/luis_/OneDrive/Escritorio/Archivos ejemplo python/csv_example.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employess:
        writer.writerow(row)
    print(f"csv file {file_path} was created.")