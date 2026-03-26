"""
Assignment 2: File Handling and Exception Handling
ITP2 | SE-2057 | Arnur & Marat
"""
import csv
import os
from typing import List, Tuple


def read_grades(filename: str) -> List[Tuple[str, float]]:
    """Read student grades from a CSV file.

    Expected CSV format (no header):
        Alice,88.5
        Bob,92.0

    Returns:
        List of (name, grade) tuples.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if a grade value cannot be converted to float.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    grades = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 2:
                continue
            name = row[0].strip()
            try:
                grade = float(row[1].strip())
            except ValueError:
                raise ValueError(f"Invalid grade for '{name}': {row[1]!r}")
            grades.append((name, grade))
    return grades


def write_grades(filename: str, grades: List[Tuple[str, float]]) -> None:
    """Write student grades to a CSV file.

    Args:
        filename: Path to the output CSV file.
        grades: List of (name, grade) tuples.
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for name, grade in grades:
            writer.writerow([name, f"{grade:.1f}"])


def average_grade(grades: List[Tuple[str, float]]) -> float:
    """Compute the average grade.

    Raises:
        ValueError: if grades list is empty.
    """
    if not grades:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(g for _, g in grades) / len(grades)


def top_student(grades: List[Tuple[str, float]]) -> str:
    """Return the name of the student with the highest grade.

    Raises:
        ValueError: if grades list is empty.
    """
    if not grades:
        raise ValueError("No grades available.")
    return max(grades, key=lambda x: x[1])[0]


def main():
    sample_file = "grades.csv"

    # Write sample data
    sample_grades = [
        ("Alice", 88.5),
        ("Bob", 92.0),
        ("Carol", 76.0),
        ("Dave", 95.5),
    ]
    write_grades(sample_file, sample_grades)
    print(f"Wrote {len(sample_grades)} records to '{sample_file}'.")

    # Read back
    try:
        grades = read_grades(sample_file)
        print(f"\nGrades loaded ({len(grades)} students):")
        for name, grade in grades:
            print(f"  {name}: {grade}")

        print(f"\nAverage grade : {average_grade(grades):.2f}")
        print(f"Top student   : {top_student(grades)}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Data error: {e}")
    finally:
        # Clean up sample file
        if os.path.exists(sample_file):
            os.remove(sample_file)


if __name__ == "__main__":
    main()
