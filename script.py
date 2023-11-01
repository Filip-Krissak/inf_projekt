import json

file_name = "data.json"

# Read data from the JSON file or initialize it as an empty dictionary
try:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {"data": []}

# Input data (You can uncomment the input lines and remove the static values if you prefer user input)
date = "2023-07-04"
bottle_can = True
user = "Gregor"
amount = 7

# Create a new action entry
new_data = {
    "user": user,
    "date": date,
    "bottle_can": bottle_can,
    "amount": amount
}

data["data"].append(new_data)

# Save the updated data back to the JSON file with new lines
with open(file_name, "w") as json_file:
    json.dump(data, json_file, separators=(',', ': '))

print(data)
