"""Программа преобразования csv-фавйла в словарь json для перевода ПД."""

import pandas as pd
import json


json_file = 'C:\\for the job\\Orlov\\orlov_side_effects.json'
csv_file = ('C:\\for the job\\Orlov\\cleaпed_orlov_translation.csv')

df = pd.read_csv(csv_file, sep=';')

result_dict = df.set_index('оригинал')['перевод'].to_dict()
print(result_dict)

with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(result_dict, file, indent=4, ensure_ascii=False)

print('Работа программы успешно завершина!')
