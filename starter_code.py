import csv
import os
import random

# Task: understand each line before running
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True) # Creates folder if not present

filepath = os.path.join(data_dir, 'students_scores.csv')

names = ['Aisha', 'Daniyar', 'Zarina', 'Arman', 'Gulnur',
         'Bekzat', 'Saltanat', 'Nursultan', 'Madina', 'Yerlan',
         'Aizat', 'Timur', 'Moldir', 'Azat', 'Diana',
         'Sanzhar', 'Ainur', 'Marat', 'Kamila', 'Dauren']
genders = ['Female', 'Male', 'Female', 'Male', 'Female',
           'Male', 'Female', 'Male', 'Female', 'Male',
           'Female', 'Male', 'Female', 'Male', 'Female',
           'Male', 'Female', 'Male', 'Female', 'Male']
groups = ['SE-101', 'SE-101', 'SE-102', 'SE-102', 'SE-103',
          'SE-103', 'SE-101', 'SE-102', 'SE-103', 'SE-101',
          'SE-102', 'SE-103', 'SE-101', 'SE-102', 'SE-103',
          'SE-101', 'SE-102', 'SE-103', 'SE-101', 'SE-102']

with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['student_id','name','gender','group',
        'math_score','python_score','english_score'])

    for i, name in enumerate(names):
        writer.writerow([
            i + 1, name, genders[i], groups[i],
            random.randint(45, 100),
            random.randint(40, 100),
            random.randint(50, 100)
        ])

print(f'Dataset saved to: {os.path.abspath(filepath)}')