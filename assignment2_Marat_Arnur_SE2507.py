import os
import csv
import sys

data_dir = 'data'

# Task 1
os.makedirs(data_dir, exist_ok=True)

filepath = os.path.join(data_dir, 'students_scores.csv')

if os.path.exists(filepath):
    abs_path = os.path.abspath(filepath)
    print(f"File found: {abs_path}")
    print(f"Absolute path: {abs_path}")
else:
    print('Error: File not found')
    sys.exit(1)

# Task 2
