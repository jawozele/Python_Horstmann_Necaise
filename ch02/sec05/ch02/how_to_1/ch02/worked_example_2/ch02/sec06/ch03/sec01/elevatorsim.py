# # This program simulates an elevator panel that skips the 13th floor
#
# # Obtain the floor number from the user as an integer
#
# floor = int(input("Floor: "))
#
# # Adjust floor if neccesary
#
# if floor > 13:
#     actualFloor = floor - 1
# else:
#     actualFloor = floor
#
# # Print the result
#
# print("The elevator will travel to the actual floor", actualFloor)

originalPrice = 110
if originalPrice < 90:
    originalPrice = originalPrice - 10
    discount = originalPrice
    print(originalPrice)
else:
    print("Sorry the real retail price for the product is greater than 100 \nOn this occasion there will be no discount offered.")