attendees = ["Aurelie", "Benjamin", "Nadja"]
attendees.append("David")
attendees.extend(["Sebastien", "Helene"])
optional_invitees = ["Magda", "Hubert"]

potential_attendees = attendees + optional_invitees

print('There are', len(potential_attendees), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("Cc: " + cc_line)
