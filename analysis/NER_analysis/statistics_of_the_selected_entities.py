"""Модуль сбора статистических данных."""

import json
import os

from ner_statistics_collector import NERStatisticsCollector


NER_DATASET = 'C:\\for the job\\NER\\content\\data_bio_5.json'

with open(NER_DATASET, 'r', encoding='utf-8') as file:
    ner_dataset = json.load(file)

collector = NERStatisticsCollector(ner_dataset)

tags_freqs = collector.tags_frequency()
print(f'Частота каждого тега {tags_freqs}')
print(f'Общее число тегов: {collector.total_tags()}')
print(f'Относительная частота: {collector.tags_ratio()}')
print(f'Самый частый тег: {collector.max_frequency()}')
print(f'Самый редкий тег: {collector.min_frequency()}')

with open(f'statistic_from_{os.path.basename(NER_DATASET)}',
          'w',
          encoding='utf-8') as file:
    json.dump(tags_freqs, file, ensure_ascii=False, indent=4)

print('Работа программы успешно завершина!')
