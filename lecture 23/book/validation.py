from datetime import date


def input_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: this field cannot be empty!")


def input_year(prompt: str) -> int:
    current_year = date.today().year
    while True:
        raw = input(prompt).strip()
        try:
            year = int(raw)
        except ValueError:
            print("Error: year must be a number!")
            continue
        if not 1000 <= year <= current_year:
            print(f"Error: year must be between 1000 and {current_year}!")
            continue
        return year