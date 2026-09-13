# Damien Inge
# September 13, 2026
# P1HW2
# Calculate and Display Travel Expenses

budget = int(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = int(input("How much do you think you will spend on gas? "))

accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))

food = int(input("Last, how much do you need for food? "))

# Travel Expenses
print("-----Travel Expenses-----")
print()
print("Location: ", destination)
print("Initial Budget: ", budget)

print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food)

final_result = budget - gas - accomodation - food
print("Remaining Balance: ", final_result)