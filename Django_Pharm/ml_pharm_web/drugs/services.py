import os
import re

from django.conf import settings
from .models import DrugGroup
from .forms import (
    AddSideEffect, updateSeideEffectRande, DisplaySideEffectsForm
)


def get_path(filename):
    return os.path.join(settings.TXT_DB_PATH, filename)


def handle_add_drug(drug_name):
    path_drugs = get_path('drugs_xcn.txt')
    path_rangs = get_path('rangs.txt')

    with open(path_drugs, 'r', encoding='utf-8') as file:
        last_line = list(file)[-1]
        last_id = int(last_line.strip().split('\t')[0])

    with open(path_drugs, 'a', encoding='utf-8') as file:
        file.write(f'\n{last_id + 1}\t{drug_name}')

    with open(path_rangs, 'a', encoding='utf-8') as file:
        file.write('0.0\n')


def handle_add_drug_group(data):
    DrugGroup.objects.create(**data)


def get_side_effects_view(request):
    path_se = get_path('side_effects.txt')
    path_drugs = get_path('drugs_xcn.txt')
    path_rangs = get_path('rangs.txt')

    if request.method == 'POST':
        form = DisplaySideEffectsForm(request.POST)
        if form.is_valid():
            display_method = form.cleaned_data['display_method']

            if display_method == 'all':
                with open(path_se, 'r', encoding='utf-8') as file:
                    side_effects = [
                        line.split('\t')[1].replace(';', '').strip()
                        for line in file if line.strip()
                    ]
                return "all", "Побочные эффекты", side_effects, form

            all_side_effects = []
            with open(path_se, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split('\t')
                        all_side_effects.append({'index': parts[0], 'name': parts[1]})

            with open(path_rangs, 'r', encoding='utf-8') as file:
                rangs = [line.strip() for line in file if line.strip()]

            drug_index = None
            drug_name = None
            with open(path_drugs, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('\t')
                    if display_method == parts[0]:
                        drug_index = int(parts[0]) - 1
                        drug_name = parts[1]
                        break

            if drug_index is None:
                return None, "Лекарство не найдено", [], form

            with open(path_se, 'r', encoding='utf-8') as file:
                total_se = sum(1 for line in file if line.strip())

            start = drug_index * total_se
            end = start + total_se
            drug_rangs = rangs[start:end]

            side_effects = [
                {
                    "index": all_side_effects[i]['index'],
                    "name": all_side_effects[i]['name'],
                    "rang": float(drug_rangs[i])
                }
                for i in range(total_se)
            ]

            return "drug", drug_name, side_effects, form

    form = DisplaySideEffectsForm()

    return None, None, None, form


def get_add_side_effect_form(request):
    path_se = get_path('side_effects.txt')
    path_drugs = get_path('drugs_xcn.txt')
    path_rangs = get_path('rangs.txt')

    with open(path_drugs, 'r', encoding='utf-8') as file:
        drug_count = len([line for line in file if line.strip()])

    with open(path_se, 'r', encoding='utf-8') as file:
        lines = [line for line in file if line.strip()]
        last_line = lines[-1]
        last_id = int(last_line.strip().split('\t')[0])

    se_count = len(lines)

    if request.method == 'POST':
        form = AddSideEffect(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            if not re.search(r'[a-zA-Zа-яА-Я]', name):
                return AddSideEffect()

            with open(path_rangs, 'r', encoding='utf-8') as file:
                rangs = [line for line in file if line.strip()]

            def insert_after_every_n(lst, new_elem, n, total):
                result = []
                for i in range(0, len(lst), n):
                    result.extend(lst[i:i+n])
                    if len(result) // (n+1) < total:
                        result.append(new_elem)
                return result

            rangs = insert_after_every_n(rangs, '0.0\n', se_count, drug_count)

            with open(path_rangs, 'w', encoding='utf-8') as file:
                file.writelines(rangs)

            with open(path_se, 'a', encoding='utf-8') as file:
                file.write(f"\n{last_id + 1}\t{name}\t0.0")

    else:
        form = AddSideEffect()

    return form


def get_update_side_effect_form(request, drug_id):
    path_se = get_path('side_effects.txt')
    path_rang = get_path('rangs.txt')
    path_drugs = get_path('drugs_xcn.txt')

    with open(path_se, 'r', encoding='utf-8') as file:
        side_effects = [line.strip().split('\t') for line in file if line.strip()]

    with open(path_drugs, 'r', encoding='utf-8') as file:
        drug_true_id = None
        for line in file:
            parts = line.strip().split('\t')
            if parts[1] == drug_id:
                drug_true_id = int(parts[0]) - 1
                break

    with open(path_rang, 'r', encoding='utf-8') as file:
        rangs = [line.strip() for line in file if line.strip()]

    if request.method == 'POST':
        form = updateSeideEffectRande(request.POST)
        if form.is_valid():
            rang = form.cleaned_data.get('name').replace(',', '.')
            se_id = int(form.cleaned_data.get('display_method')) - 1
            se_count = len(side_effects)
            index = drug_true_id * se_count + se_id
            rangs[index] = rang

            with open(path_rang, 'w', encoding='utf-8') as file:
                file.write('\n'.join(rangs) + '\n')
    else:
        form = updateSeideEffectRande()
        
    return form
