# Create a list of places to visit
places_to_visit = ["dubai", "sharjah", "ajman", "abu dhabi", "ras al khaimah"]

# Print the list in its original order
print("Original order:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the original list
print("Alphabetical order:", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original order:", places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original order
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original order:", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Use reverse() again to change the order back to the original
places_to_visit.reverse()
print("Original order:", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Alphabetical order:", places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order:", places_to_visit)