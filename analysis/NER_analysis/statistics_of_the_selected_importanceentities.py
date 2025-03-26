"""Модуль сбора статистических данных."""

import json
import os

from importance_and_ner_statistics_collector import (
    ImportanceNERStatisticsCollector)


NER_IMPORTANCE_DATASETS = [
    ('C:\\for the job\\experiment_with_ner\\content'
     '\\modifite_info_for_test_models_0.json'),
    ('C:\\for the job\\experiment_with_ner\\content'
     '\\modifite_info_for_test_models_1.json'),
    ('C:\\for the job\\experiment_with_ner\\content'
     '\\modifite_info_for_test_models_2.json'),
    ]

for dataset in NER_IMPORTANCE_DATASETS:
    with open(dataset, 'r', encoding='utf-8') as file:
        ner_dataset = json.load(file)

    collector = ImportanceNERStatisticsCollector(ner_dataset)

    result_statistic = {
        'Частота каждого тега': collector.tags_frequency(),
        'Общее число тегов': collector.total_tags(),
        'Относительная частота': collector.tags_ratio(),
        'Самый частый тег': collector.max_frequency(),
        'Самый редкий тег': collector.min_frequency(),
        'Частота признаков важности': collector.importance_frequency(),
        'Общая частота признаков важности': collector.importance_total(),
        'Относительная частота признаков важности':
        collector.importance_relative_frequency()
    }

    with open(f'statistic_from_{os.path.basename(dataset)}',
              'w',
              encoding='utf-8') as file:
        json.dump(result_statistic, file, ensure_ascii=False, indent=4)

print('Работа программы успешно завершина!')
