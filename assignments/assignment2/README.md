# Assignment 2: File Handling and Exception Handling

## Description

Build a simple student grade manager that reads and writes data to CSV files,
using proper exception handling throughout.

## Tasks

1. Implement `read_grades(filename)` — reads a CSV file and returns a list of `(name, grade)` tuples.
2. Implement `write_grades(filename, grades)` — writes a list of `(name, grade)` tuples to a CSV file.
3. Implement `average_grade(grades)` — computes the average grade; raises `ValueError` for empty input.
4. Implement `top_student(grades)` — returns the name of the student with the highest grade.
5. Handle `FileNotFoundError` and `ValueError` gracefully in the main program.

## How to Run

```bash
python grade_manager.py
```
