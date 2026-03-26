"""
Tests for Assignment 2: File Handling and Exception Handling
"""
import os
import pytest
from grade_manager import read_grades, write_grades, average_grade, top_student


@pytest.fixture
def tmp_csv(tmp_path):
    """Return a temporary CSV file path."""
    return str(tmp_path / "grades.csv")


class TestReadGrades:
    def test_reads_valid_file(self, tmp_csv):
        with open(tmp_csv, "w", encoding="utf-8") as f:
            f.write("Alice,88.5\nBob,92.0\n")
        grades = read_grades(tmp_csv)
        assert grades == [("Alice", 88.5), ("Bob", 92.0)]

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            read_grades("/nonexistent/path/grades.csv")

    def test_invalid_grade_raises(self, tmp_csv):
        with open(tmp_csv, "w", encoding="utf-8") as f:
            f.write("Alice,not_a_number\n")
        with pytest.raises(ValueError):
            read_grades(tmp_csv)


class TestWriteGrades:
    def test_write_and_read_back(self, tmp_csv):
        grades = [("Alice", 88.5), ("Bob", 92.0)]
        write_grades(tmp_csv, grades)
        result = read_grades(tmp_csv)
        assert result == grades

    def test_creates_file(self, tmp_csv):
        write_grades(tmp_csv, [("X", 70.0)])
        assert os.path.exists(tmp_csv)


class TestAverageGrade:
    def test_average(self):
        grades = [("A", 80.0), ("B", 90.0), ("C", 70.0)]
        assert average_grade(grades) == pytest.approx(80.0)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            average_grade([])


class TestTopStudent:
    def test_top_student(self):
        grades = [("Alice", 88.5), ("Bob", 92.0), ("Carol", 76.0)]
        assert top_student(grades) == "Bob"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            top_student([])
