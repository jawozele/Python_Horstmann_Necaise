# This program prints the price per ounce for a six-pack of cans


# Define constant for pack size

CANS_PER_PACK = 6

# Obtain price per pack and can volume
userInput = input("Please enter the price for a six-pack: ")
packPrice = float(userInput)



userInput = input("Please enter the volume for each can (in ounces): ")
canVolume = float(userInput)

packVolume = canVolume * CANS_PER_PACK

# Compute pack volume
pricePerOunce = packPrice / packVolume
print("Price per ounce: %8.2f" % pricePerOunce)