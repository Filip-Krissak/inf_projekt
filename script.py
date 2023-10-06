import json

filename = "data.json"
# date = input("Enter the date (e.g., '2023-10-05'): ")
# bottle_can = input("Is it a bottle (True) or can (False): ").lower() == 'true'
# user = input("Enter the user's name: ")
# amount = int(input("Enter the quantity: "))
date = "2023-10-05"
bottle_can = True
user = "Petr"
amount = 5

data = {
    "date": date,
    "bottle_can": bottle_can,
    "user": user,
    "amount": amount
}

with open(filename, "a") as json_file:
    json.dump(data, json_file)
    json_file.write("\n")

print("Data has been saved to data.json")
