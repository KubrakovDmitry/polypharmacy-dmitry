"""Программа для сопоставления назвваний ПД."""

import json


origin = ('C:\\for the job\\the_drugs_collections'
          '\\side_effects_translation.json')
corrected = ('C:\\for the job\\the_drugs_collections'
             '\\corrected_side_effects_translation.json')

with open(origin, 'r', encoding='utf-8') as file:
    original_translation = json.load(file)
with open(corrected, 'r', encoding='utf-8') as file:
    corrected_translation = json.load(file)
print(set(original_translation.keys()) == set(corrected_translation.keys()))
