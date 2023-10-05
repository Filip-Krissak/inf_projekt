import json

filename = "data.json"
# datum = input("Enter the date (e.g., '2023-10-05'): ")
# flasa_plechovka = input("Is it a bottle (True) or can (False): ").lower() == 'true'
# uzivatel = input("Enter the user's name: ")
# kusy = int(input("Enter the quantity: "))
datum = "2023-10-05"
flasa_plechovka = True
uzivatel = "Petr"
kusy = 5

data = {
    "datum": datum,
    "flasa_plechovka": flasa_plechovka,
    "uzivatel": uzivatel,
    "kusy": kusy
}

with open(filename, "w") as json_file:
    json.dump(data, json_file,indent=4)

print("Data has been saved to data.json")
