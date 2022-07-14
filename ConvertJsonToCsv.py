import json
import csv

test_dict = {("Anzahl von Kandidaten")}

with open("candidates.json", "r") as file:
    data = json.load(file)
    candidates = data["Data"]

with open("candidates.csv", "w") as file:
    candidate_count = candidates.count(candidates)
    fieldnames = test_dict[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(candidate_count)
