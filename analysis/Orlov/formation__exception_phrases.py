INTPUT_FILE = 'C:\\for the job\\Orlov\\corrected_orlov_translation.csv'
OUTPUT_FILE = 'C:\\for the job\\Orlov\\exception_phrases.txt'

exception_phrases = []
with open(INTPUT_FILE, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if '!!!' in line:
            print('line =', line)
            print('line.replace("!!!", ";").split()[0] =', line.replace('!!!', '').split(';')[0])
            exception_phrases.append(line.replace('!!!', '').split(';')[0])
with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
    for phrase in exception_phrases:
        print(phrase, file=file)
print('Работа программа успешно завершина!')
