# Original list of people to invite to dinner
invitees = ["syed", "haider", "hussain", "shah"]

# Notify that only two people can be invited
print("I can invite only two people for dinner.")

# Use pop() to remove guests until only two names remain
while len(invitees) > 2:
    removed_guest = invitees.pop()
    print("Sorry, " + removed_guest + ". I can't invite you to dinner.")

# Print a message to the two people still on the list
for person in invitees:
    print("Dear " + person + ", you are still invited to dinner.")

# Use del to remove the last two names
del invitees[:]
print("The guest list is now empty:", invitees)