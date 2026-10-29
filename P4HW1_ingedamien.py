# Damien Inge
# 10/29/2026
# P4 HW 1
# Collect module grades, validates scores, drops the lowest score, and calculates the average and letter grade.

# Prompt for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create list for scores
module_scores = []

# Prompt for grades and validate each score
for integer in range(num_scores):
    score = float(input(f"Enter score #{integer + 1}: "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{integer + 1} again: "))

    module_scores.append(score)

# Display results
lowest_grade = min(module_scores)

print("-------------Results-------------")
print(f"Lowest Grade: {lowest_grade}")

# Remove the lowest score
module_scores.remove(lowest_grade)

print(f"Score List after dropping lowest score: {module_scores}")

# Calculate average of modified list
sum_result = sum(module_scores)
average_result = sum_result / len(module_scores)

print(f"Average: {average_result:.2f}")

# Determine letter grade
if average_result >= 90:
    letter_grade = "A"
elif average_result >= 80:
    letter_grade = "B"
elif average_result >= 70:
    letter_grade = "C"
elif average_result >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Letter Grade: {letter_grade}")
print("--------------------------------------")