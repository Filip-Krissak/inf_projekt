import json
import os

# Function to load existing data from a JSON file or create a new empty database
def load_database(filename):
    data = {}
    if os.path.isfile(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Error: The JSON file is not valid. Creating a new empty database.")
    return data

# Function to save data to a JSON file
def save_database(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add an activity to a user
def add_activity(database, user, date, activity, bottle_can, amount):
    if user not in database:
        database[user] = []
    
    activity_entry = {
        "date": date,
        "activity": activity,
        "bottle_can": bottle_can,
        "amount": amount
    }
    
    database[user].append(activity_entry)

# Main program
if __name__ == "__main__":
    filename = 'database.json'
    database = load_database(filename)

    while True:
        print("Options:")
        print("1. Add activity")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = input("Enter user name: ")
            date = input("Enter date (e.g., 2023-10-05): ")
            activity = input("Enter activity: ")
            bottle_can = input("Enter bottle_can (True or False): ").lower() == 'true'
            amount = int(input("Enter amount: "))
            add_activity(database, user, date, activity, bottle_can, amount)
            save_database(database, filename)
            print(f"Added activity '{activity}' for user '{user}' on {date}.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
