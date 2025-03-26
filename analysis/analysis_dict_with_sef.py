import json
import os


DIR = 'C:\\for the job\\parser\\se_freqs'
SERIOUS_KEY = 'serious'
OTHOR_KEY = 'other'


# def recur_bypass(data):
#     result = []
#     if isinstance(data, str):
#         print('data - строка!')
#         return result.append(data)
#     elif isinstance(data, list):
#         print()\

first_keys = set()
second_keys = set()

lv = False
line = False
string = False
empty = False

for filename in os.listdir(DIR):
    with open(os.path.join(DIR, filename)) as file:
        data = json.load(file)
    if isinstance(data, str):
        line = True
        print(filename, 'содержит только строку.')
    if isinstance(data, list):
        string = True
        print(filename, 'содержит только список.')
    if isinstance(data, dict):
        print(filename, 'содержит словарь.')
        print('ключи первого порядка:', data.keys())
        first_keys.update(data.keys())
        for k in data.keys():
            print('ключи второго порядка порядка:', data[k].keys())
            second_keys.update(data[k].keys())
            for k2 in data[k].keys():
                if len(data[k][k2]) == 0:
                    empty = True
    if not (SERIOUS_KEY in data and OTHOR_KEY in data):
        lv = True


if line:
    print('есть строки!')
if string:
    print('есть списки!')
if empty:
    print('есть пустые списки!')
if lv:
    print('есть словари без нужных ключей!')
print('first_keys', first_keys)
print('second_keys', second_keys)
print('Работа программы успешно завершина!')
