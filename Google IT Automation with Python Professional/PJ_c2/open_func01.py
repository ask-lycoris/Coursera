# Creating Initial clients file
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
# Append new clients
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# Checking reservation list
guests_to_check = ['Bob', 'Andrea', 'Molly', 'Jacob']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print(f"Shown up: {check.strip()}")
        else:
            print(f"No show: {check.strip()}")
    for check in guests_to_check:
        if check in checked_in:
            print(f"Shown up: {check.strip()}")
        else:
            print(f"No show: {check.strip()}")
