import json
import pandas as pd


# json_file = 'side_effects.json'
# csv_file = ('C:\\for the job\\comparison_origin_translation_side_effects'
#             '\\translation.csv')
json_file = 'side_effects.json'
csv_file = ('C:\\for the job\\comparison_origin_translation_side_effects'
            '\\translation.csv')

with open(json_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
df = pd.read_csv(csv_file, sep=';')
csv_data = df['оригинал'].to_list()
print(len(set(json_data)-set(csv_data)))
