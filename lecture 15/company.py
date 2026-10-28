import csv
from typing import Any

with open("ssl_companies.csv", "r") as file:
    reader = csv.DictReader(file, fieldnames=",")
    for row in reader:
        employees: dict[str | Any, str | Any]=row
        print(row)