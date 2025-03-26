import os
import json


DIR = 'correct_dict_side_effects_frequency'
OUTPUT = 'unique_side_effects.json'
NAMES = 'drug_names.json'
SIDE_EFFECTS = 'side_effects'
DRUG_NAME = 'drug_name'

side_effects = set()
drugs = []

for file_name in os.listdir(DIR):

    with open(os.path.join(DIR, file_name)) as file:
        data = json.load(file)

    drugs.append(data[DRUG_NAME])
    data = data[SIDE_EFFECTS]

    for system in data.keys():
        for frequency in data[system].keys():
            for side_effect in data[system][frequency]:
                if side_effect:
                    side_effects.add(side_effect.strip())

print(len(drugs))
with open(NAMES, 'w', encoding='utf-8') as file:
    json.dump(drugs, file, indent=4, ensure_ascii=False)

with open(OUTPUT, 'w', encoding='utf-8') as file:
    json.dump(list(side_effects), file, indent=4, ensure_ascii=False)

print('Работа программа успешно завершена!')
