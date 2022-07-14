import json
import csv
from datetime import datetime
from sqlite3 import Timestamp
import this
from numpy import datetime_as_string

import pandas as pd

test_dict = {("Anzahl von Kandidaten")}

with open("candidates.json", "r") as file:
    data = json.load(file)
    candidates = data["Data"]
    number_of_candidates = len(candidates)


now = datetime.now()
date_as_string = now.strftime("%d.%m.%y")

df = pd.DataFrame(list())

file_name_with_date = f'dinos_meta_data_{date_as_string}.csv'
df.to_csv(file_name_with_date)

with open(file_name_with_date, "w") as csv_file:
    output = csv.writer(csv_file, delimiter=',')
    output.writerows([
        ['Datum', 'Anzahl Kandidaten'],
        [date_as_string, number_of_candidates],
    ])
