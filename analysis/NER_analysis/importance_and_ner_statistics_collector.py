"""Модуль сборщика статистики тегов NER и важности."""

from collections import Counter

from ner_statistics_collector import NERStatisticsCollector


class ImportanceNERStatisticsCollector(NERStatisticsCollector):
    """Сборщик статистики NER и важности."""

    SENTENCES = 'sents_info'
    TOKENS = 'tokens'
    TAGS = 'tags'
    IMPORTANCE = 'need_ratio'
    TOGETHER = 'Вместе'
    IMPORTANCE_VALUE_TRUE = 1
    IMPORTANCE_VALUE_FALSE = 0
    CONVERTER = {
        1: 'Важно',
        0: 'Неважно'
    }

    def tags_frequency(self):
        """Частота каждого тега."""
        all_tags_importance = [
            tag for item in self._dataset
            for sent in item[self.SENTENCES]
            for tag in sent[self.TAGS]
            if sent[self.IMPORTANCE] == self.IMPORTANCE_VALUE_TRUE]
        all_tags_not_importance = [
            tag for item in self._dataset
            for sent in item[self.SENTENCES]
            for tag in sent[self.TAGS]
            if sent[self.IMPORTANCE] == self.IMPORTANCE_VALUE_FALSE]

        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            Counter(all_tags_importance),
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            Counter(all_tags_not_importance),
            self.TOGETHER:
            Counter(all_tags_importance + all_tags_importance)
        }

    def total_tags(self):
        """Общее число тегов в соответсвии с важностью."""
        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            sum(len(sent[self.TAGS])
                for item in self._dataset
                for sent in item[self.SENTENCES]
                if sent[self.IMPORTANCE] == self.IMPORTANCE_VALUE_TRUE),
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            sum(len(sent[self.TAGS])
                for item in self._dataset
                for sent in item[self.SENTENCES]
                if sent[self.IMPORTANCE] == self.IMPORTANCE_VALUE_FALSE),
            self.TOGETHER:
            sum(len(sent[self.TAGS])
                for item in self._dataset
                for sent in item[self.SENTENCES])
        }

    def tags_ratio(self):
        """Соотношение тегов с учётом важности."""
        freqs = self.tags_frequency()
        total = self.total_tags()

        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            {
                tag: count / total[self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]]
                for tag, count in freqs[self.CONVERTER[
                    self.IMPORTANCE_VALUE_TRUE]].items()
            },
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            {
                tag: count / total[self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]]
                for tag, count in freqs[self.CONVERTER[
                    self.IMPORTANCE_VALUE_FALSE]].items()
            },
            self.TOGETHER:
            {
                tag: count / total[self.TOGETHER]
                for tag, count in freqs[self.TOGETHER].items()
            }
        }

    def max_frequency(self):
        """Получение самый частых тегов."""
        tags_counter_importance = (
            self.tags_frequency()[self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]])
        tags_counter_not_importance = (
            self.tags_frequency()[self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]])
        tags_counter_together = (
            self.tags_frequency()[self.TOGETHER])
        max_freq_importance = max(tags_counter_importance.values())
        max_freq_not_importance = max(tags_counter_not_importance.values())
        max_freq_together = max(tags_counter_together.values())

        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            [tag for tag, freq in tags_counter_importance.items()
             if freq == max_freq_importance],
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            [tag for tag, freq in tags_counter_not_importance.items()
             if freq == max_freq_not_importance],
            self.TOGETHER:
            [tag for tag, freq in tags_counter_together.items()
             if freq == max_freq_together]
        }

    def min_frequency(self):
        """Получение самый частых тегов."""
        tags_counter_importance = (
            self.tags_frequency()[self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]])
        tags_counter_not_importance = (
            self.tags_frequency()[self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]])
        tags_counter_together = (
            self.tags_frequency()[self.TOGETHER])
        min_freq_importance = min(tags_counter_importance.values())
        min_freq_not_importance = min(tags_counter_not_importance.values())
        max_freq_together = min(tags_counter_together.values())
        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            [tag for tag, freq in tags_counter_importance.items()
             if freq == min_freq_importance],
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            [tag for tag, freq in tags_counter_not_importance.items()
             if freq == min_freq_not_importance],
            self.TOGETHER:
            [tag for tag, freq in tags_counter_together.items()
             if freq == max_freq_together]
        }

    def importance_frequency(self):
        """Метод получения частоты признаков важности."""
        freqs = Counter([sent[self.IMPORTANCE]
                         for item in self._dataset
                         for sent in item[self.SENTENCES]])
        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            freqs[self.IMPORTANCE_VALUE_TRUE],
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            freqs[self.IMPORTANCE_VALUE_FALSE]
        }

    def importance_total(self):
        """Метод получения общей частоты важности."""
        return len([
            sent[self.IMPORTANCE]
            for item in self._dataset
            for sent in item[self.SENTENCES]
        ])

    def importance_relative_frequency(self):
        """Метод получения относительной частоты важности."""
        imp_total = self.importance_total()
        imp_freq = self.importance_frequency()
        return {
            self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]:
            imp_freq[self.CONVERTER[self.IMPORTANCE_VALUE_TRUE]]/imp_total,
            self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]:
            imp_freq[self.CONVERTER[self.IMPORTANCE_VALUE_FALSE]]/imp_total
        }
