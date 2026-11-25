import os
from datetime import datetime

# Get the folder where this Python script is saved
folder = os.path.dirname(os.path.abspath(__file__))

# Set the diary file location
diary_file = os.path.join(folder, "diary.txt")

try:
    # Check if the diary file exists
    if not os.path.exists(diary_file):
        with open(diary_file, "w", encoding="utf-8") as file:
            pass
        print("New diary file created.")

    # Ask the user to enter a diary entry
    entry = input("Enter your diary entry: ")

    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the new entry to the diary file
    with open(diary_file, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}: {entry}\n")

    print("\nDiary entry saved successfully!")

    # Read and display all diary entries
    with open(diary_file, "r", encoding="utf-8") as file:
        print("\n===== ALL DIARY ENTRIES =====")
        print(file.read())

except OSError as error:
    print("File operation error:", error)
