# Damien Inge
# 10/12/2026
# P3HW1
# Fix and complete the program so it runs correctly.


# This program takes a number grade , determines average and displays letter grade for average.

import math

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
print()
mod_2 = float(input("Enter grade for Module 2: "))
print()
mod_3 = float(input("Enter grade for Module 3: "))
print()
mod_4 = float(input("Enter grade for Module 4: "))
print()
mod_5 = float(input("Enter grade for Module 5: "))
print()
mod_6 = float(input("Enter grade for Module 6: "))
print()

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low_grades = min(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
high_grades = max(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
sum = mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6
avg = sum/6

print("-------------Results-------------")
print(f"Lowest Grade: {low_grades}")
print(f"Highest Grade: {high_grades}")
print(f"Sum of Grades: {sum}")
print(f"Average: {avg:.2f}")
print("--------------------------------------")

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
        print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
else:
     print("You need improvement.")



