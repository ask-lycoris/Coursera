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
