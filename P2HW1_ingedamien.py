#Damien Inge
#9/27/2026
#P2HW1
#Edit and enhance exiting programs

budget = float(int(input("Enter Budget: ")))

destination = input("Enter your travel destination: ")

gas = float(int(input("How much do you think you will spend on gas? ")))

accomodation = float(int(input("Approximately, how much will you need for accomodation/hotel? ")))

food = float(int(input("Last, how much do you need for food? ")))

# Travel Expenses
print("-----Travel Expenses-----")
print()
print(f'{"Location: ":<20s}', destination)
print(f'{"Initial Budget: ":<20s} ${budget:.2f}')

print(f'{"Fuel: ":<20s} ${gas:.2f}')
print(f'{"Accomodation: ":<20s} ${accomodation:.2f}')
print(f'{"Food: ":<20s} ${food:.2f}')

final_result = budget - gas - accomodation - food
print(f'{"Remaining Balance: ":<20s} ${final_result:.2f}')
