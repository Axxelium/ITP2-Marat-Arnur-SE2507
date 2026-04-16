import os
import csv
import pandas as pd
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

print()

# Task 2
with open(filepath, mode='r', encoding='utf-8') as csv_file:

    reader = csv.DictReader(csv_file)

    print(f"Fields: {reader.fieldnames}")

    ctr_reader = 0
    for row in reader:

        if ctr_reader < 5:
            print(f"Row {ctr_reader + 1}: {row}")

        ctr_reader += 1

    print(f"Total students: {ctr_reader}")

print()

# Task 3
# 3a: Load
df = pd.read_csv(filepath)

print(df.head())
print("Shape:" , df.shape)
print(df.dtypes)

# 3b: Statistics
print(df.describe())

print()
# 3c: Add average column
df['average_score'] = df[['math_score', 'python_score', 'english_score']].mean(axis=1).round(2)
print(df[['name', 'group', 'average_score']])

print()
# 3d: Filtering
high_scorers = df[ df['average_score'] >= 75  ]
group_101 = df[ df['group'] == 'SE-101'  ]

print(high_scorers)
print(group_101)

print()

# 3e: Group analysis
group_means = df.groupby('group')[['math_score','python_score','english_score']].mean()
gender_means = df.groupby('gender')['average_score'].mean()
print(group_means)
print(gender_means)




