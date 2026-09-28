#Damien Inge
#9/27/2026
#P2HW2
#Write a program that asks the user to enter test grades for modules, using a separate input statement for each one

import math

#Prompt for Grades
module_1 = float(input("Enter grade for Module 1: "))
print()
module_2 = float(input("Enter grade for Module 2: "))
print()
module_3 = float(input("Enter grade for Module 3: "))
print()
module_4 = float(input("Enter grade for Module 4: "))
print()
module_5 = float(input("Enter grade for Module 5: "))
print()
module_6 = float(input("Enter grade for Module 6: "))
print()

module_scores = [module_1, module_2, module_3, module_4, module_5, module_6]

#Display results

lowest_grade = min(module_1, module_2, module_3, module_4, module_5, module_6)
highest_grade = max(module_1, module_2, module_3, module_4, module_5, module_6)
sum_result = module_1 + module_2 + module_3 + module_4 + module_5 + module_6
average_result = sum_result/6

print("-------------Results-------------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_result}")
print(f"Average: {average_result:.2f}")
print("--------------------------------------")
