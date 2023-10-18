# Cost of a single USB stick and the total budget
usb_stick_price = 6
budget = 50

# Calculate the number of USB sticks she can buy
num_usb_sticks = budget // usb_stick_price

# Calculate the pounds left after buying USB sticks
pounds_left = budget % usb_stick_price

# Display the results
print("She can buy", num_usb_sticks, "USB sticks.")
print("She will have £", pounds_left, "left.")