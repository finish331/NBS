import json

with open("reference.json", 'r') as load_f:
  load_dict = json.load(load_f)

RepeatPlayer = []

print(load_dict[0])