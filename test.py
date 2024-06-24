import json

processes_file = '/afs/cern.ch/user/c/ccarriva/ZZHH/processes.json'
decay_file = '/afs/cern.ch/user/c/ccarriva/ZZHH/decay.json'

process = "zhjj"

with open(processes_file, 'r') as file:
    processes_data = json.load(file)

with open(decay_file, 'r') as file:
    decay_data = json.load(file)

br_expression = processes_data.get(process, {}).get('BR')

for key, value in decay_data.items():
    br_expression = br_expression.replace(key, str(value))

calculated_br = eval(br_expression)
print(f"L'espressione BR per il processo {process} è: {calculated_br}")
