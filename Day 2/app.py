# Basic tip calculator
print("Welcome to the tip calculator\nWhat was the total bill? ")
bill = float(input())

print("How much tip would you like to give? ")
tip = float(input())

print("How many people to split the bill? ")
people = float(input())

tipf = bill * (tip/100)
billf = bill + tipf
per_person = billf/people

# print(tipf)
# print(billf)
# print(per_person)

print(f"Each person should pay ${per_person}")