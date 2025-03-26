"""Модуль создания списка унальных сущностей."""

import json
import re


SOURCE = 'data_log_6.json' # 'data_log_5_1.json'
FINAL = 'unique_entities_2.json'
ENTITIES = 'entities'

with open(SOURCE, 'r', encoding='utf-8') as file:
    data = json.load(file)

# заменить на dev
replace_action = lambda text: re.sub(r'\s*-\s*', '-', text)

unique_entities = [(replace_action(entity[0].strip().lower()), entity[1])
                   for item in data for sent in item
                   for entity in sent[ENTITIES]]

with open(FINAL, 'w', encoding='utf-8') as file:
    json.dump(unique_entities, file, ensure_ascii=False, indent=4)

print('Список уникальных сущностей составлем!')
