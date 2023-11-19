rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")

# Loop to print the name of each river included in the dictionary
for river in rivers.keys():
    print(river.capitalize())

# Loop to print the name of each country included in the dictionary
for country in rivers.values():
    print(country.capitalize())