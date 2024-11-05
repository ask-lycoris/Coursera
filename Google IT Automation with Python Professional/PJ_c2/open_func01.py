# Python Build-in Functions [https://docs.python.org/3/library/functions.html#built-in-functions]
# * open(x,x) function [https://docs.python.org/3/library/functions.html#open]

# r:  read only (default)
# w:  write only    ---> noted!! the previous file will be overwrited which means get deleted as soon as we open the file, so better to use append mode with log files.
# a:  append
# r+: read or write  ---> noted!! ??? なにが注意すべき点か言及されていなかった気がする。
# x:  open for exclusive creation, failing if the file already exists
# なんかもうちょっと詳しく勉強したいなここ

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
