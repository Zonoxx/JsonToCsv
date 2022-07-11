import json
import csv

with open("candidates.json", "r") as file:
    data = json.load(file)
    candidates = data["Data"]

with open("candidates.csv", "w") as file:
    fieldnames = candidates[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for field in candidates:
        writer.writerow(field)
