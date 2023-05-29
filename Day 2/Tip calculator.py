# Day 2 - Make a tipping calculator which calculates the total bill based on the amount due, the people splitting the
# bill and how much you would like to tip

# function to calculate how much should each person pay taking in total, #people, and how much tip
def amount_due(total, people, tip):
    return round((total / people) * (1 + tip/100), 2)

def tipcalculator():
    total = float(input("Welcome to my tip calculator!\nHow much is the total bill?\n"))
    people = int(input("How many people will the bill be split against?\n"))
    tip = float(input("How much would you like to tip?\n"))
    print("Each person should tip: " + str(amount_due(total,people,tip)))

tipcalculator()