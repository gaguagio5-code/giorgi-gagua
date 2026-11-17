
from builtins import ValueError

ALLOWED_GRADES = ("A", "B", "C", "D", "F")

def validate_name(value):
    """Return a cleaned name or raise ValueError."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Name must be a non-empty text.")
    return value.strip()

def validate_roll_number(value):
    """Return the roll number as a positive int or raise ValueError."""
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError("Roll number must be a whole number.")
    try:
        number = int(value)
    except ValueError:
        raise ValueError("Roll number must be a whole number.") from None
    if number <= 0:
        raise ValueError("Roll number must be greater than 0.")
    return number

def validate_grade(value):
    """Return the grade as an upper-case single letter or raise ValueError."""
    if not isinstance(value, str):
        raise ValueError("Grade must be a single letter.")
    grade = value.strip().upper()
    if len(grade) != 1 or grade not in ALLOWED_GRADES:
        allowed = ", ".join(ALLOWED_GRADES)
        raise ValueError(f"Grade must be one of: {allowed}.")
    return grade

class Person:
    """Base class: anything that has a name."""

    def __init__(self, name):
        self.name = name  # goes through the property setter below

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_name(value)

    def __str__(self):
        return f"Name: {self.name}"

class Student(Person):
    """A student with a name, a roll number and a letter grade."""

    def __init__(self, name, roll_number, grade):
        super().__init__(name)
        self.roll_number = roll_number
        self.grade = grade

    @property
    def roll_number(self):
        return self._roll_number

    @roll_number.setter
    def roll_number(self, value):
        self._roll_number = validate_roll_number(value)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = validate_grade(value)

    def __str__(self):
        # Polymorphism: overrides Person.__str__ and extends it.
        return f"Roll Number: {self.roll_number} | {super().__str__()} | Grade: {self.grade}"


class StudentManager:
    """Stores students and performs the operations on them (no input/output here)."""

    def __init__(self):
        self._students = {}  # roll_number -> Student

    def add_student(self, student):
        if student.roll_number in self._students:
            raise ValueError(f"A student with roll number {student.roll_number} already exists.")
        self._students[student.roll_number] = student

    def get_all_students(self):
        return [self._students[key] for key in sorted(self._students)]

    def find_by_roll_number(self, roll_number):
        """Return the Student or None if not found."""
        return self._students.get(roll_number)

    def update_grade(self, roll_number, new_grade):
        student = self.find_by_roll_number(roll_number)
        if student is None:
            raise ValueError(f"No student with roll number {roll_number}.")
        student.grade = new_grade

class ConsoleApp:
    """Handles the menu and all user input/output."""

    MENU = (
        "\n===== Student Management System =====\n"
        "1. Add a new student\n"
        "2. View all students\n"
        "3. Find a student by roll number\n"
        "4. Update a student's grade\n"
        "5. Exit"
    )

    def __init__(self, manager):
        self._manager = manager

    @staticmethod
    def _ask(prompt, validator):
        """Keep asking until the validator accepts the input."""
        while True:
            try:
                return validator(input(prompt))
            except ValueError as error:
                print(f"Invalid input: {error}")

    def _add_student(self):
        name = self._ask("Enter name: ", validate_name)
        while True:
            roll_number = self._ask("Enter roll number: ", validate_roll_number)
            if self._manager.find_by_roll_number(roll_number) is None:
                break
            print(f"Roll number {roll_number} is already taken. Try another one.")
        grade = self._ask("Enter grade (A, B, C, D, F): ", validate_grade)
        self._manager.add_student(Student(name, roll_number, grade))
        print("Student added successfully.")

    def _view_all(self):
        students = self._manager.get_all_students()
        if not students:
            print("No students in the system yet.")
            return
        print("\n All students ")
        for student in students:
            print(student)

    def _find_student(self):
        roll_number = self._ask("Enter roll number to search: ", validate_roll_number)
        student = self._manager.find_by_roll_number(roll_number)
        print(student or f"No student with roll number {roll_number}.")

    def _update_grade(self):
        roll_number = self._ask("Enter roll number of the student: ", validate_roll_number)
        student = self._manager.find_by_roll_number(roll_number)
        if student is None:
            print(f"No student with roll number {roll_number}.")
            return
        print(f"Current: {student}")
        new_grade = self._ask("Enter new grade (A, B, C, D, F): ", validate_grade)
        self._manager.update_grade(roll_number, new_grade)
        print("Grade updated successfully.")

    def run(self):
        actions = {
            "1": self._add_student,
            "2": self._view_all,
            "3": self._find_student,
            "4": self._update_grade,
        }
        while True:
            print(self.MENU)
            choice = input("Choose an option (1-5): ").strip()
            if choice == "5":
                print("Goodbye!")
                break
            action = actions.get(choice)
            if action is None:
                print("Invalid choice. Please enter a number from 1 to 5.")
            else:
                action()

def main():
    ConsoleApp(StudentManager()).run()

if __name__ == "__main__":
    main()