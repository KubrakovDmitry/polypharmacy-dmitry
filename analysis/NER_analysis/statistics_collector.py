"""Модуль абстрактного сборщика статистика."""

from abc import (ABC,
                 abstractmethod)


class StatisticsCollector(ABC):
    """Абстрактный класс сборщика статистики."""

    def __init__(self, dataset=None):
        """Конструктор сборщика статистики."""
        self._dataset = dataset

    @property
    def dataset(self):
        """Геттер датасета."""
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Сеттер датасета."""
        self._dataset = dataset

    @abstractmethod
    def tags_frequency(self):
        """Частота каждого тега."""

    @abstractmethod
    def total_tags(self):
        """Общее число тегов."""

    @abstractmethod
    def tags_ratio(self):
        """Соотношение тегов."""

    @abstractmethod
    def max_frequency(self):
        """Получение самый частых тегов."""

    @abstractmethod
    def min_frequency(self):
        """Получение самых редких тегов."""
