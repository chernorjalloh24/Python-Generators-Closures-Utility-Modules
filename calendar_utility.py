import calendar
from datetime import datetime

try:
    # Ask the user for a year and month
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))

    # Check if the year and month are valid
    if year < 1 or year > 9999:
        print("Error: Enter a year between 1 and 9999.")

    elif month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")

    else:
        # Display the calendar
        print("\n===== MONTHLY CALENDAR =====")
        print(calendar.month(year, month))

        # Get today's date
        today = datetime.now()

        print("Today's Date:", today.strftime("%B %d, %Y"))

        # Check if today is in the selected month
        if today.year == year and today.month == month:
            print("Today is in the selected month!")
            print("Today is", today.strftime("%B %d, %Y"))
        else:
            print("Today is not in the selected month.")

except ValueError:
    print("Error: Please enter valid numbers.")
