import json


PATH1 = 'C:\\for the job\\making_dataset_interactions\\interactions_ru.json'
PATH2 = 'C:\\for the job\\the_drugs_collections\\drug_names_en_ru.json'
with open(PATH1, 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(PATH2, 'r', encoding='utf-8') as file:
    data2 = json.load(file)
names1 = set()
for key in data.keys():
    names1.update(key.replace('\n', '').replace(' ', '-').lower().split('_'))

names2 = set()
for key in data2.keys():
    names2.add(key)

# print(names1)
# print(names2)
print('Совпадение есть?', names1 <= names2)
