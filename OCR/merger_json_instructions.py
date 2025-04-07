"""Модулуль сливания инструкций в один json-словарь."""

from pathlib import Path
import json
import os
import sys


class JSONMerger:
    """Класс слияния."""

    def __init__(self, path):
        """Конструктор."""
        self.__path = path

    @property
    def path(self):
        """Геттер."""
        return self.__path

    @path.setter
    def path(self, path):
        """Сеттер."""
        self.__path = path

    def __walk(self):
        """Метод обхода директории с файлами."""
        for file in os.listdir(self.__path):
            if file.endswith('.json'):
                yield os.path.join(self.__path, file)
        # return [os.path.join(self.path, file) for file in os.listdir(self.path)
        #         if file.endswith('.json')]

    def __save(self):
        """Метод сохранения."""
        path = f'{self.__path}.json'
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.unified,
                      file,
                      ensure_ascii=False,
                      indent=4)
        print(f"Единная коллекция успешно сохранена в файл {path}!")

    def merge(self):
        """Метод слияния."""
        self.unified = []
        for path in self.__walk():
            with open(path, 'r', encoding='utf-8') as file:
                self.unified.append({
                    'ЛС': Path(path).stem,
                    'текст инструкции': json.load(file)
                })
        self.__save()


def main():
    """Тело программы."""
    merger = JSONMerger(sys.argv[1])
    merger.merge()
    print('Слияние произведена успешно!')


if __name__ == '__main__':
    main()
