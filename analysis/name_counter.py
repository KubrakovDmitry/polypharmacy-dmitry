import json


PATH = 'C:\\for the job\\making_dataset_interactions\\interactions_ru.json'

with open(PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)


names = set()
for key in data.keys():
    names.update(key.replace('\n', '').split('_'))

print('Число названий:', len(names))