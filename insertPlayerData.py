import json

with open("./python/players.json", 'r') as load_f:
  load_dict = json.load(load_f)
print(load_dict[1]['name'])
print(len(load_dict))