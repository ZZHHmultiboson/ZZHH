import json

# Leggi il file JSON
with open('operators.json', 'r') as file:
    operators = json.load(file)

# Filtra gli operatori con "turn" uguale a "on"
name_list = [key for key, value in operators.items() if value["turn"] == "on"]

print(name_list)
