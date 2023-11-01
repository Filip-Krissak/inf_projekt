import json

file_name = "data.json"

try:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {"data": []}

date = "2023-07-04"
bottle_can = True
user = "Gregor"
amount = 7

new_data = {
    "user": user,
    "date": date,
    "bottle_can": bottle_can,
    "amount": amount
}

data["data"].append(new_data)

with open(file_name, "w") as json_file:
    json.dump(data, json_file, separators=(',', ': '))

print(data)
