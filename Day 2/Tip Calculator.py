from art import logo
print(logo)

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
tip_percent = tip/100
people = int(input("How many people to split the bill? "))
total_tip_amount = tip_percent * bill
total_bill = bill + total_tip_amount
amount_split = round((total_bill/people), 2)
print(f"Each person should pay: {amount_split}.")
