### Q1
#sample1
import re

def compare_strings(string1, string2):
    # Convert both strings to lowercase and remove leading/trailing spaces
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # Define punctuation and escape the hyphen
    punctuation = r"[.?!,;:\-\']"  # Escape '-' using '\'

    # Remove punctuation
    string1 = re.sub(punctuation, r"", string1)
    string2 = re.sub(punctuation, r"", string2)

    # Compare the normalized strings
    return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False


### Q2
# sample2
import datetime
from datetime import date

def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        # Handles the Leap Year case (February 29)
        new_date_obj = date_obj.replace(year=date_obj.year + 4)
    return new_date_obj

def next_date(date_string):
    # Convert the argument from string to date object
    date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d").date()
    next_date_obj = add_year(date_obj)

    # Convert the datetime object to string, in the format of "yyyy-mm-dd"
    next_date_string = next_date_obj.strftime("%Y-%m-%d")
    return next_date_string

# Test Cases
today = date.today()  # Get today's date
today_string = today.strftime("%Y-%m-%d")  # Format today's date as a string

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29


### Q2
# sample2
from datetime import datetime, timedelta

def add_year(date_obj):
    print(f"Debug: Starting add_year with date_obj: {date_obj}")  # Debugging
    try:
        # Try to add one year directly
        return date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        # Handle leap year case (February 29)
        print("Debug: Adjusting for leap year.")  # Debugging
        return date_obj + timedelta(days=365 * 4)  # Move to next possible leap year

def next_date(date_string):
    print(f"Debug: Starting next_date with date_string: {date_string}")  # Debugging
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    print(f"Debug: Parsed date_obj: {date_obj}")  # Debugging
    next_year_date = add_year(date_obj)
    print(f"Debug: Calculated next_year_date: {next_year_date}")  # Debugging
    return next_year_date.strftime("%Y-%m-%d")

# Test Cases
print(next_date("2020-02-29"))  # Leap year case
print(next_date("2021-03-01"))  # Regular case

