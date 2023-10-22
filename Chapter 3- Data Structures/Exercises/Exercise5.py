# Original list of people to invite to dinner
invitees = ["syed", "haider", "hussain"]

# One guest can't make it, so you decide to invite someone else
cancelled_guest = "hussain"  # Replace with the name of the guest who can't make it
new_guest = "shah"  # The person you're inviting in place of the cancelled guest

# Remove the cancelled guest and add the new guest
invitees.remove(cancelled_guest)
invitees.append(new_guest)

# Send out the updated invitations
for person in invitees:
    print("Dear " + person + ", you are cordially invited to dinner at my place.")