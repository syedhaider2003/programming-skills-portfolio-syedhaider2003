# Make several dictionaries
dog = {
    'kind': 'dog',
    'owner': 'Alice'
}

cat = {
    'kind': 'cat',
    'owner': 'Bob'
}

fish = {
    'kind': 'fish',
    'owner': 'Charlie'
}

# Store these dictionaries in a list called pets
pets = [dog, cat, fish]

# Loop through your list and print everything you know about each pet
for pet in pets:
    print(f"{pet['owner'].capitalize()} has a {pet['kind'].capitalize()}.")