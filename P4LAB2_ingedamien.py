# Damien Inge
# 10/29/2026
# P4 LAB2
# Use while loop and for loop together

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))
    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else: 
        print("This program does not handle negative values.")

    run_again = input("Would you like to run the program again? ")

print("Program is ending...")