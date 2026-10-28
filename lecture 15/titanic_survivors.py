import csv


def read_survived(titanic):
    file = open(titanic.csv, "r", encoding="utf-8", newline="")
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    survived = []
    for row in reader:
        if row["survived"] == "1":
            survived.append(row)

    file.close()
    return fieldnames, survived


def write_survived(filename, fieldnames, passengers):
    file = open(filename, "w", encoding="utf-8", newline="")
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(passengers)
    file.close()


def read_titanic():
    pass
read_titanic()
write_survived(filename='titanic.csv', passengers="1")
print(f"Surviving Passengers: {len("1")}")