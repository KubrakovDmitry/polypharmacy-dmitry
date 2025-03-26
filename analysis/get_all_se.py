import json
import os


DIR = 'C:\\for the job\\parser\\se_freqs'
SERIOUS_KEY = 'serious'
OTHER_KEY = 'other'

all_side_effects = []

for filename in os.listdir(DIR):
    with open(os.path.join(DIR, filename), 'r', encoding='utf-8') as file:
        data = json.load(file)
    for k in data[SERIOUS_KEY].keys():
        all_side_effects.extend(data[SERIOUS_KEY][k])
    for k2 in data[OTHER_KEY].keys():
        all_side_effects.extend(data[OTHER_KEY][k2])

with open('side_effects.json', 'w', encoding='utf-8') as file:
    json.dump(all_side_effects, file)

print('Работа программы завершина!')
