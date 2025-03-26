import json
import os


DIR = 'new_side_effects_frequency'
NEW_DIR = 'correct_dict_side_effects_frequency'
# DIR = 'C:\\for the job\\Orlov\\side_effects_frequency'
SIDE_EFFECTS = 'side_effects'


side_effects = set()

for filename in os.listdir(DIR):

    with open(os.path.join(DIR, filename), 'r', encoding='utf-8') as file:
        data = json.load(file)

    for system in data[SIDE_EFFECTS].keys():
        for frequency in data[SIDE_EFFECTS][system].keys():
            data[SIDE_EFFECTS][system][frequency] = (
                data[SIDE_EFFECTS][system][frequency][0])

    with open(os.path.join(NEW_DIR, filename), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

print('Работа программы успешно завершина!')
