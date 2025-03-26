import pandas as pd
import json


INPUT = ('C:\\for the job\\comparison_origin_translation_side_effects'
         '\\translation.csv')
OUTPUT = 'side_effects_translation.json'

df = pd.read_csv(INPUT, delimiter=';')
unduplicated = df.drop_duplicates()
print(len(unduplicated))
translation_dict = unduplicated.set_index('оригинал')['перевод'].to_dict()
print(translation_dict)
print(len(translation_dict))
with open(OUTPUT, 'w', encoding='utf-8') as file:
    json.dump(translation_dict, file, ensure_ascii=False, indent=4)
print('Работа программы успешно завершина!')
