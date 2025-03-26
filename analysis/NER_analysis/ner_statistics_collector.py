"""Модуль класса сборщика статистических данных о NER."""

from collections import Counter

from statistics_collector import StatisticsCollector


class NERStatisticsCollector(StatisticsCollector):
    """Класс сборщика статистики."""

    TOKENS = 'tokens'
    TAGS = 'tags'

    def __init__(self, dataset=None):
        """Конструктор сборщика статистики."""
        super().__init__(dataset)

    def tags_frequency(self):
        """Частота каждого тега."""
        all_tags = [tag for item in self._dataset
                    for tag in item[self.TAGS]]
        return Counter(all_tags)

    def total_tags(self):
        """Общее число тегов."""
        return sum(len([item[self.TAGS] for item in self._dataset]))

    def tags_ratio(self):
        """Соотношение тегов."""
        freqs = self.tags_frequency()
        total = self.total_tags()
        return {tag: count / total for tag, count in freqs.items()}

    def max_frequency(self):
        """Получение самый частых тегов."""
        tags_counter = self.tags_frequency()
        max_freq = max(tags_counter.values())
        return [tag for tag, freq in tags_counter.items() if freq == max_freq]

    def min_frequency(self):
        """Получение самых редких тегов."""
        tags_counter = self.tags_frequency()
        min_freq = min(tags_counter.values())
        return [tag for tag, freq in tags_counter.items() if freq == min_freq]

    def get_entities(self):
        """Полный уникальный список сущностей."""
        return {tag for item in self._dataset for tag in item[self.TOKENS]}
