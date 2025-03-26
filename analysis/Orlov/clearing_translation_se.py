INTPUT_FILE = 'C:\\for the job\\Orlov\\corrected_orlov_translation.csv'
OUTPUT_FILE = 'C:\\for the job\\Orlov\\cleaпed_orlov_translation.csv'

with open(INTPUT_FILE, 'r', encoding='utf-8') as input:
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as output:
        for line in input.readlines():
            if '!!!' in line:
                continue
            print(line, end='', file=output)
print('Работа программа успешно завершина!')
