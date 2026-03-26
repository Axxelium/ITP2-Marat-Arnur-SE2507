# Task 1
task1_name = str(input('Enter your name: '))
task1_age = int(input('Enter your age: '))

print(f"Hello, {task1_name} ! You are years {task1_age} old.")

# Task 2
task2_fn = float(input("Enter first number: "))
task2_sn = float(input("Enter second number: "))
print("Sum:", task2_fn + task2_sn)
print("Difference:", task2_fn - task2_fn)
print("Product:", task2_fn * task2_sn)

# Task 3
task3_C = int(input("Enter your temperature in Celsius: "))
task3_F= task3_C * 9 / 5 + 32
print ("Temperature in Fahrenheit:", task3_F)

# Task 4
task4_a = int(input("Enter first number: "))
task4_b = int(input("Enter second number: "))
task4_temp = task4_a
task4_a = task4_b
task4_b = task4_temp

print(task4_b - task4_a)

# Task 5
task5_a = int(input("Enter first number: "))
if task5_a / 2:
    print('Even')
else:
    print('Odd')

# Task 6
task6_age = int(input("Enter your age: "))
if 0 <= task6_age <= 12:
    print("Child")
elif 13 <= task6_age <= 17:
    print("Teenager")
elif task6_age >= 18:
    print("Adult")
else:
    print("Invalid age")

# Task 7
task7_a = float(input("Enter first number: "))
task7_b = float(input("Enter second number: "))
task7_c = float(input("Enter third number: "))
if task7_a >= task7_b and task7_a >= task7_c:
    print("Largest:", task7_a)
elif task7_b >= task7_a and task7_b >= task7_c:
    print("Largest:", task7_b)
else:
    print("Largest:", task7_c)

# Task 8
task8_num1 = float(input("Enter first number: "))
task8_num2 = float(input("Enter second number: "))
task8_op = input("Enter operation (+, -, *, /): ")
if task8_op == "+":
    print("Result:", task8_num1 + task8_num2)
elif task8_op == "-":
    print("Result:", task8_num1 - task8_num2)
elif task8_op == "*":
    print("Result:", task8_num1 * task8_num2)
elif task8_op == "/":
    if task8_num2 != 0:
        print("Result:", task8_num1 / task8_num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")

# Task 9
task9_year = int(input("Enter a year: "))
if (task9_year % 4 == 0 and task9_year % 100 != 0) or (task9_year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Task 10
task10_score = int(input("Enter a score (0-100): "))
if 90 <= task10_score <= 100:
    print("A")
elif 75 <= task10_score <= 89:
    print("B")
elif 50 <= task10_score <= 74:
    print("C")
elif 0 <= task10_score < 50:
    print("F")
else:
    print("Invalid score")

# Task 11
task11_balance = 1000
task11_withdraw = float(input("Enter withdrawal amount: "))
if task11_withdraw <= task11_balance:
    task11_balance -= task11_withdraw
    print("Success! Remaining balance:", task11_balance)
else:
    print("Error: Insufficient funds")

# Task 12
task12_login_sys = "admin"
task12_password_sys = "1234"
task12_login_input = input("Enter login: ")
task12_password_input = input("Enter password: ")
if task12_login_input == task12_login_sys and task12_password_input == task12_password_sys:
    print("Access granted")
else:
    print("Invalid credentials")

# Task 13
task13_amount = float(input("Enter purchase amount: "))
if task13_amount >= 10000:
    print("Discount 10%. Final amount:", task13_amount * 0.9)
elif task13_amount >= 5000:
    print("Discount 5%. Final amount:", task13_amount * 0.95)
else:
    print("No discount. Final amount:", task13_amount)

# Task 14
task14_a = float(input("Enter side 1: "))
task14_b = float(input("Enter side 2: "))
task14_c = float(input("Enter side 3: "))
if task14_a + task14_b > task14_c and task14_a + task14_c > task14_b and task14_b + task14_c > task14_a:
    if task14_a == task14_b == task14_c:
        print("Equilateral triangle")
    elif task14_a == task14_b or task14_b == task14_c or task14_a == task14_c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Triangle does not exist")

# Task 15
task15_color = input("Enter traffic light color: ").lower()
if task15_color == "red":
    print("Stop")
elif task15_color == "yellow":
    print("Wait")
elif task15_color == "green":
    print("Go")
else:
    print("Invalid color")

# Task 16
task16_num = int(input("Enter a number: "))
if task16_num > 0:
    print("Positive")
elif task16_num < 0:
    print("Negative")
else:
    print("Zero")

if task16_num % 2 == 0:
    print("Even")
else:
    print("Odd")

if 1 <= task16_num <= 100:
    print("Within range 1-100")
else:
    print("Out of range 1-100")

# Task 17
task17_num1 = float(input("Enter first number: "))
task17_num2 = float(input("Enter second number: "))
task17_op = input("Enter operation (+, -, *, /, **, %): ")
if task17_op == "+":
    print(task17_num1 + task17_num2)
elif task17_op == "-":
    print(task17_num1 - task17_num2)
elif task17_op == "*":
    print(task17_num1 * task17_num2)
elif task17_op == "**":
    print(task17_num1 ** task17_num2)
elif task17_op == "/":
    if task17_num2 != 0:
        print(task17_num1 / task17_num2)
    else:
        print("Error: Division by zero")
elif task17_op == "%":
    if task17_num2 != 0:
        print(task17_num1 % task17_num2)
    else:
        print("Error: Modulo by zero")
else:
    print("Error: Invalid operation")

# Task 18
task18_pwd = input("Enter your password: ")
task18_has_digit = any(char.isdigit() for char in task18_pwd)
task18_has_upper = any(char.isupper() for char in task18_pwd)
task18_is_long = len(task18_pwd) >= 8

if task18_is_long and task18_has_digit and task18_has_upper:
    print("Strong")
elif task18_is_long and (task18_has_digit or task18_has_upper):
    print("Medium")
else:
    print("Weak")

# Task 19
task19_balance = 5000
print("1 - Check balance\n2 - Deposit\n3 - Withdraw")
task19_choice = input("Select an option: ")

if task19_choice == "1":
    print("Your balance:", task19_balance)
elif task19_choice == "2":
    task19_deposit = float(input("Enter deposit amount: "))
    task19_balance += task19_deposit
    print("Success. New balance:", task19_balance)
elif task19_choice == "3":
    task19_withdraw = float(input("Enter withdrawal amount: "))
    if task19_withdraw <= task19_balance:
        task19_balance -= task19_withdraw
        print("Success. New balance:", task19_balance)
    else:
        print("Error: Insufficient funds")
else:
    print("Invalid option")

# Task 20
task20_secret = 7
task20_guess = int(input("Guess the secret number: "))
if task20_guess > task20_secret:
    print("Too high")
elif task20_guess < task20_secret:
    print("Too low")
else:
    print("Correct")

# Task 21
task21_score = int(input("Enter exam score: "))
task21_attendance = int(input("Enter attendance (%): "))
if task21_score < 50 or task21_attendance < 60:
    print("Fail")
else:
    if task21_score >= 90:
        print("A")
    elif task21_score >= 75:
        print("B")
    else:
        print("C")

# Task 22
task22_amount = float(input("Enter order amount: "))
task22_distance = float(input("Enter distance (km): "))
task22_cost = 1000

if task22_amount > 15000:
    task22_cost = 0
elif task22_distance > 5:
    task22_cost += (task22_distance - 5) * 200

print("Delivery cost:", task22_cost)

# Task 23
task23_salary = float(input("Enter salary: "))
task23_history = input("Enter credit history (good/bad): ").lower()
if task23_salary > 200000 and task23_history == "good":
    print("Approved")
else:
    print("Rejected")

# Task 24
task24_attempts = 2
task24_login = "Arnur"
task24_password = 1234

if task24_attempts <= 2:
    task24_attempt1_login = str(input('Enter your login'))
    task24_attempt1_password = int(input('Enter your password'))
    if task24_attempt1_login == task24_login and task24_attempt1_password == task24_password:
        print("Success")
    else:
        print("Error")
else:
    print("Your attempts ended!")

# Task 25
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Exit Execute based on user choice using conditions.')
task25_choice = int(input("Select an option: "))

if task25_choice == 1:
    task24_a = int(input('first number: '))
    task24_b = int(input('second number: '))
    print('Add', task24_a + task24_b)
elif task25_choice == 2:
    task24_a = int(input('first number: '))
    task24_b = int(input('second number: '))
    print('Subtract', task24_a - task24_b)
elif task25_choice == 3:
    task24_a  = int(input('first number: '))
    task24_b = int(input('second number: '))
    print('Multiply', task24_a * task24_b)
elif task25_choice == 4:
    print("Goodbye!")
else:
    print("Invalid option")

