# This program prints a description of an earthquake, given the Richter scale magnitude

# Obtain the user input

Richter = float(input("Enter a magnitude on the Richter scale: "))

# Print the description

if Richter >= 8.0:
    print("Most structures fall")
elif Richter >= 7.0:
    print("Many buildings destroyed")
elif Richter >= 6.0:
    print("Many buildings considerably damaged, some collapse")
elif Richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No description of buildings")