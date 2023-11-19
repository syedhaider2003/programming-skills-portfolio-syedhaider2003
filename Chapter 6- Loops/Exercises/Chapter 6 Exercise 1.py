# Define an empty list called toppings
toppings = []

# Keep asking the user for a topping until they enter 'quit'
while True:
    topping = input("Enter a topping for your pizza ('quit' to stop): ").lower()
    
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Added {topping.capitalize()} to your pizza.")

# Print a final message showing all the toppings that will be added to the pizza
print(f"Your pizza will have the following toppings: {', '.join(topping.capitalize() for topping in toppings)}")