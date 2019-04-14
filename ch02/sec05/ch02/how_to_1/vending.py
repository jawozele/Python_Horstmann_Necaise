# This program simulates a vending machine that gives change

# Define constants

PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

# Obtain user input

userInput = input("Please enter bill value (1  = $1, 5 = $5 bill, etc.): ")
billValue = int(userInput)
userInput = input("Please enter item price in pennies: ")
itemPrice = int(userInput)

# Compute change due
changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice
dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue % PENNIES_PER_DOLLAR
quarters = changeDue // PENNIES_PER_QUARTER

# Print change due
print("Dollar coins: %6d" % dollarCoins)
print("Quarters: %6d" % quarters)