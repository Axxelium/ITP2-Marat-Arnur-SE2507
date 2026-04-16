import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


# Task 4

# Plot 1: Bar chart
group_avg = df.groupby('group')['average_score'].mean()
plt.figure(figsize=(8, 5))
plt.bar( group_avg.index, group_avg.values , color=['#3498DB','#E74C3C','#2ECC71'])
plt.title('Average Score by Study Group')
plt.xlabel('Study Group')
plt.ylabel('Average Score')
plt.savefig(os.path.join(data_dir, 'bar_group_avg.png'), dpi=150,
bbox_inches='tight')
plt.show()

# Plot 2: Histogram
group_python = df['python_score']
plt.figure(figsize=(8, 5))
plt.hist(group_python, bins=10, color='#9B59B6', edgecolor='white')
plt.title('Distribution of Python Scores')
plt.xlabel('Python Score')
plt.ylabel('Number of Students')
plt.savefig(os.path.join(data_dir, 'hist_python_scores.png'), dpi=150,
bbox_inches='tight')
plt.show()

# Plot 3: Box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='gender', y='average_score', palette='Set2')
plt.title('Score Distribution by Gender')
plt.savefig(os.path.join(data_dir, 'box_gender_scores.png'), dpi=150,
bbox_inches='tight')
plt.show()

# Plot 4: Heatmap
plt.figure(figsize=(8, 6))
corr = df[['math_score','python_score','english_score','average_score']].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix of Student Scores')
plt.savefig(os.path.join(data_dir, 'heatmap_correlation.png'), dpi=150,
bbox_inches='tight')
plt.show()

