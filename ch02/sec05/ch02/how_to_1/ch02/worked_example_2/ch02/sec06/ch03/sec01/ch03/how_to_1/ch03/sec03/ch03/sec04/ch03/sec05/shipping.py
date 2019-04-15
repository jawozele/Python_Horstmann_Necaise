# A program to compute shipping costs

# Obtain the user input

country = input("Enter the country: ")
state = input("Enter the State or Province: ")

# Compute the shipping cost

shippingcost = 0.0
if country == "USA":
    if state =="AK" or state == "MI":
        shippingCost = 5.0
    else:
        shippingCost = 10.0
print("Shipping cost to {},{}, is {}".format(state, country, shippingCost))