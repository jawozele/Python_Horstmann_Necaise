# This program computes the volume (in liters) of a six-pack of soda
# cans and the total volume of a six-pack and a two liter bottle

CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0

# Number of cans per pack

cansPerPack = 4

# Calculate total volume in the cans

totalVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "liters.")

# Calculate total volume in the cans and a two-liter bottle

totalVolume = totalVolume + BOTTLE_VOLUME
print("A six-pack and a two-liter bottle contains", totalVolume, "liters")


# # Assignment
#
# 1. CASE_BOTTLES
# 2. per liter cannot be used in place of variale.
#     The accepted standard is per_liter

unitPrice = 5
quantity = 4
totalPurchasePrice = unitPrice * quantity
print(" The total purchase price for this app is {}".format(totalPurchasePrice))


# Total volume cannot be a constant variable because
# this is used to call the other 2 variables which would
# require the application to run

