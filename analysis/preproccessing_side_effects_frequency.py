import os
import re


SOURCE_DIR = 'C:\\for the job\\Orlov\\side_effects_frequency'
FINAL_DIR = 'new_side_effects_frequency'

for filename in os.listdir(SOURCE_DIR):
    with open(os.path.join(SOURCE_DIR, filename),
              'r',
              encoding='utf-8') as file:
        text = file.read()
        text = re.sub(r'\(.*?\)', '', text)
        with open(os.path.join(FINAL_DIR, filename),
                  'w',
                  encoding='utf-8') as output:
            output.write(text)
